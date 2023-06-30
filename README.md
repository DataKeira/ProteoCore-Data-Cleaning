# ProteoCore Data Cleaning Dash App

The ProteoCore Data Cleaning Dash App is a web application that allows users to clean and process proteomics data to prepare it for programs such as MetaboAnalyst. It provides an interactive interface to filter data based on the target species, remove unwanted columns, and intensity values for gene entries.

## How to Use

1. **Enter Target Species**: Specify the target species for data filtering. Only rows with the specified species in the "Organism" column will be included in the analysis. For example (Homo sapien OX=9606), include both the species and OX number.

2. **Input CSV File**: Enter the file path or URL to the CSV file containing your proteomics data. The app will read the data from this file.

3. **Output CSV File Name**: Provide a name for the output CSV file where the cleaned data will be saved. The app will generate a new CSV file with the cleaned data.

4. **Clean Data**: Click the "Clean Data" button to process the data based on the specified target species and column filtering. The cleaned data will be displayed in the text area below.

5. **Output**: The cleaned data will be displayed in the text area below the "Clean Data" button. It will also be saved as a new CSV file with the provided output file name.

## Dependencies

- Python 3.6 or higher
- pandas 2.0.3
- dash 2.11.0
- dash-core-components
- dash-html-components
- Jupyter is NOT required to run this app

## How to Run

To run the ProteoCore Data Cleaning Dash App, follow these steps:

1. Clone or download this GitHub repository.

2. Install the required Python packages using pip:

```bash
pip install pandas dash dash-core-components dash-html-components
```

3. Open the terminal or command prompt, navigate to the directory where the app code is located, and run the app:

```bash
gunicorn -w 4 data_cleaning:app
```

4. Open a web browser and go to the following address to access the Dash app:

```
http://127.0.0.1:8050/
```

## Note

- Make sure to have the CSV file containing the proteomics data in the correct format with required columns such as "Organism," "Gene," and "Intensity" columns.

- The app will fill empty values in the "Gene" column with the "Entry Name" value for identification.

- The app will remove rows where all columns except the "Gene" column have a value of 0.

- Columns containing "MaxLFQ" or "Unique" in their names will be excluded from the analysis.

- Duplicates will be aggragated instead of dropped.

- If you wish to add labels to your sample columns you must do so manually onto the output csv file.

- Does not remove keratin contamination if your target species is Human.

## Feedback and Contributions

Your feedback and contributions to this project are highly appreciated! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

