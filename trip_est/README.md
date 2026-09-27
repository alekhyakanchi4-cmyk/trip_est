# Indian Trip Cost Estimator

This project is a Flask-based web application for calculating the estimated travel cost for a trip in India. It includes vehicle fuel cost, stay cost, food cost, and misc expenses, along with a visual breakdown using Chart.js.

## Features
- One-way distance input in kilometers
- Number of persons and trip duration input
- Vehicle type selection with average mileage presets
- Fuel price and daily expense inputs
- Auto-calculated round-trip total cost
- Per-person cost estimate
- Doughnut and bar charts for visual analysis
- Clean responsive web interface

## Project Structure

```text
trip_est/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── .gitignore
```

## Technologies Used
- Python
- Flask
- HTML, CSS, JavaScript
- Chart.js

## Step-by-Step VS Code Execution

### 1. Open the project in VS Code
- Open VS Code.
- Click File > Open Folder.
- Select the folder: `trip_est`

### 2. Open a terminal in VS Code
- Go to Terminal > New Terminal
- Make sure the terminal opens in the project folder

### 3. Create a virtual environment
If Python is installed and recognized by your system, use:

```bash
python -m venv venv
```

On many Windows systems, use this instead:

```bash
py -m venv venv
```

### 4. Activate the virtual environment
For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

If pip is not recognized, use:

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Flask application
```bash
python app.py
```

If `python` does not work, use:

```bash
py app.py
```

### 7. Open the app in the browser
After the server starts, open:

```text
http://127.0.0.1:5000
```

### 8. Use the calculator
- Enter trip parameters
- Click Calculate & Generate Charts
- View total trip cost and chart breakdown

## Example Input
- One-way Distance: 350 km
- Persons: 4
- Days: 3
- Vehicle: Hatchback
- Fuel Price: ₹102/l
- Stay Rate: ₹2500/room/night
- Food Budget: ₹600/person/day
- Misc: ₹1200

## Notes
- The app assumes round-trip travel cost.
- Stay cost is calculated using 2 persons per room.
- Mileage values are approximate average values for Indian travel conditions.

## B.Tech Project Idea
This project is suitable for a mini web application / project submission because it combines:
- backend logic using Python Flask
- frontend UI using HTML and JavaScript
- data visualization using Chart.js
- real-world cost estimation logic

## Troubleshooting
If the app does not run:
- Make sure Python is installed and added to PATH
- Check that the virtual environment is activated
- Reinstall dependencies using `pip install -r requirements.txt`
- Confirm the Flask server is running without errors

## License
This project is for educational and academic use.
