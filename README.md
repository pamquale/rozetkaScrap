# iPhone Scraper rozetka.com.ua

This project consists of a web scraper and a GUI application to manage iPhone model data from the website Rozetka.com.ua. The scraper extracts iPhone model information, including model name, part number, colors, RAM, price, and storage. The GUI application allows users to view, edit, and save this data.

## Project Structure

- `scraper.py`: The script to scrape iPhone model data from Rozetka.com.ua and save it to a JSON file.
- `gui.py`: The GUI application to load, display, and edit the iPhone model data from the JSON file.
- `iphone_models.json`: The JSON file that stores the scraped iPhone model data.

## Requirements

- Python 3.6 or higher
- `requests` library
- `beautifulsoup4` library
- `tkinter` library (comes with Python standard library)
- `re` library (comes with Python standard library)

## Installation

1. Clone the repository or download the project files.
2. Ensure you have Python 3.6 or higher installed on your system.
3. Install the required libraries using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

### 1. Scraping Data

1. Run the `scraper.py` script to scrape the iPhone model data from Rozetka.com.ua and save it to `iphone_models.json`:
   ```bash
   python scraper.py
   ```
2. The script will output a message indicating that the data has been successfully scraped and saved to `iphone_models.json`.

### 2. Running the GUI

1. Run the `gui.py` script to launch the GUI application:
   ```bash
   python gui.py
   ```
2. The GUI will load the data from `iphone_models.json` and display it in a table format.
3. The data can be sorted by model numbers (highest first) and allows for editing of the entries.

### GUI Features

- **View Data**: Displays the iPhone model data in a sortable table.
- **Edit Data**: Allows users to edit the model name, part number, colors, RAM, price, and storage.
- **Save Changes**: Saves the edited data back to `iphone_models.json`.

## Project Files

### scraper.py

The `scraper.py` script scrapes the iPhone model data from Rozetka.com.ua. It extracts the following fields:
- Model name
- Part number
- Colors
- RAM
- Price
- Storage

### gui.py

The `gui.py` script provides a GUI application to load, display, and edit the iPhone model data. The GUI features include:
- Loading data from `iphone_models.json`
- Displaying data in a sortable table
- Editing individual fields
- Saving changes back to `iphone_models.json`

## Example Data Format

The `iphone_models.json` file will have the following format:

```json
[
    {
        "Name": "iPhone 15 Pro",
        "Part Number": "MTV53RX/A",
        "Colors": "Titanium",
        "RAM": "8GB",
        "Price": "52 999₴",
        "Storage": "256GB"
    },
    {
        "Name": "iPhone 13",
        "Part Number": "MLPF3HU/A",
        "Colors": "Midnight",
        "RAM": "4GB",
        "Price": "24 999₴",
        "Storage": "128GB"
    },
    ...
]
```


## License

This project is licensed under the MIT License.
