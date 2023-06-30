import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Create the Dash app
app = dash.Dash(__name__)
server = app.server

# Define the app layout
app.layout = html.Div(
    children=[
        html.H1("ProteoCore Data Cleaning"),
        html.Label("Target Species"),
        dcc.Input(id="target-species-input", type="text", placeholder="Enter target species"),
        html.Label("Input CSV file"),
        dcc.Input(id="csv-file-input", type="text", placeholder="Enter CSV file path"),
        html.Label("Output CSV file name"),
        dcc.Input(id="output-file-input", type="text", placeholder="Enter output file name"),
        html.Button("Clean Data", id="clean-data-button", n_clicks=0),
        html.Div(id="cleaned-data-output")
    ]
)

@app.callback(
    Output("cleaned-data-output", "children"),
    [Input("clean-data-button", "n_clicks")],
    [State("target-species-input", "value"), State("csv-file-input", "value"), State("output-file-input", "value")]
)
def clean_data(n_clicks, target_species, csv_file, output_file):
    if n_clicks > 0:
        # Read the data from the CSV file
        df = pd.read_csv(csv_file)
        
        # Filter the data to include only rows with the target species
        filtered_data_row = df[df['Organism'] == target_species]

        #any empty values in gene will be filled with the entry name of that row for identification
        df['Gene'] = df['Gene'].fillna(df['Entry Name'])

        #setting a value to Gene and Inensity columns except MaxLFQ or Unique intensity
        columns_to_keep = ['Gene'] + [col for col in filtered_data_row.columns if 'Intensity' in col and 'MaxLFQ' not in col and 'Unique' not in col]
        
        #removes all columns except columns chosen above
        filtered_data_column = filtered_data_row[columns_to_keep]

        # Filter columns that contain the word "Intensity"
        intensity_columns = filtered_data_column.columns[filtered_data_column.columns.str.contains('Intensity')]

        # Combine the duplicate rows based on the 'Gene' column and sum the values in the intensity columns
        cleaned_data = filtered_data_column.groupby('Gene')[intensity_columns].sum().reset_index()
        
        # Check if all columns except 'Gene' have a value of 0
        mask = (cleaned_data.loc[:, cleaned_data.columns != 'Gene'] == 0).all(axis=1)

        # Filter the DataFrame to remove rows where the condition is True
        clean_data = cleaned_data[~mask]

        # Save cleaned data to CSV with the user-provided output file name
        clean_data.to_csv(output_file, index=False)

        return dcc.Textarea(value=str(clean_data), style={'width': '100%', 'height': '300px'})

    return ""

if __name__ == '__main__':
    app.run_server(debug=True)


