# Pokemon Ultra Sun Search

A simple web application to search and filter Pokemon from Pokemon Ultra Sun.

## Features

- Browse all Pokemon available in Pokemon Ultra Sun (Generations 1-7, National Dex #1-807)
- View Pokemon details including:
  - Name
  - Types (primary and secondary)
  - Evolution chain (previous and next evolutions)
  - Base stats (HP, Attack, Defense, Sp. Attack, Sp. Defense, Speed)
  - Total base stats
- **Sort by Total Stats**: Ascending or descending order
- **Filter by Type**: Select one or multiple types
- **Filter by Final Evolution**: Show only Pokemon that don't evolve further

## Installation

1. Clone the repository:
```bash
git clone https://github.com/oliviafrancislee/pokemon-ultra-sun-search.git
cd pokemon-ultra-sun-search
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Data Source

The application uses a predefined static dataset containing 149 Pokemon from Generations 1-7, representing a comprehensive sample of Pokemon available in Pokemon Ultra Sun. The data includes all starter Pokemon evolution lines, popular Pokemon from each generation, and legendary Pokemon.

## How to Use

1. **Type Filter**: Use the sidebar to select one or more Pokemon types to filter the results
2. **Final Evolutions Only**: Check this box to show only Pokemon that are fully evolved (no next evolution)
3. **Sort by Total Stats**: Choose to sort Pokemon by their total base stats in ascending or descending order
4. View detailed statistics including top performers and averages

## Requirements

- Python 3.8+
- pandas
- streamlit