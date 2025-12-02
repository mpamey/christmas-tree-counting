# 🎄 Christmas Tree Counting

A Python package for counting and analyzing Christmas trees from data files.

## Features

- 📊 Count total Christmas trees from CSV data files
- 🌲 Group and count trees by species
- 📍 Group and count trees by location
- 📏 Filter trees by height range
- 📈 Calculate average tree height
- 🎯 Generate comprehensive summary statistics
- 💻 Command-line interface for easy usage

## Installation

This package uses [Poetry](https://python-poetry.org/) for dependency management.

### Prerequisites

- Python 3.8 or higher
- Poetry (optional, for development)

### Install with Poetry

```bash
# Clone the repository
git clone https://github.com/mpamey/christmas-tree-counting.git
cd christmas-tree-counting

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### Install with pip

```bash
# Clone the repository
git clone https://github.com/mpamey/christmas-tree-counting.git
cd christmas-tree-counting

# Install the package
pip install -e .
```

## Usage

### Command Line Interface

After installation, you can use the `count-trees` command:

```bash
count-trees data/christmas_trees.csv
```

This will output a summary like:

```
==================================================
Christmas Tree Counting Summary
==================================================

Total Trees: 20

Average Height: 3.01 meters

Trees by Species:
  - Norway Spruce: 5
  - Douglas Fir: 4
  - Fraser Fir: 4
  - Noble Fir: 4
  - Blue Spruce: 3

Trees by Location:
  - North Forest: 6
  - East Garden: 5
  - West Grove: 4
  - South Meadow: 5
==================================================
```

### Python API

You can also use the package programmatically in your Python code:

```python
from christmas_tree_counting import ChristmasTreeCounter

# Initialize the counter with a data file
counter = ChristmasTreeCounter('data/christmas_trees.csv')

# Count total trees
total = counter.count_total_trees()
print(f"Total trees: {total}")

# Count by species
by_species = counter.count_by_species()
print(f"Trees by species: {by_species}")

# Count by location
by_location = counter.count_by_location()
print(f"Trees by location: {by_location}")

# Count trees in a height range (2-4 meters)
in_range = counter.count_by_height_range(min_height=2.0, max_height=4.0)
print(f"Trees between 2-4m: {in_range}")

# Get average height
avg_height = counter.get_average_height()
print(f"Average height: {avg_height:.2f} meters")

# Get comprehensive summary
summary = counter.get_summary()
print(summary)
```

## Data Format

The package expects CSV files with the following format:

```csv
tree_id,species,location,height_m,age_years,health_status
1,Norway Spruce,North Forest,2.5,5,Excellent
2,Douglas Fir,North Forest,3.2,7,Good
...
```

### Required Columns

- `species`: Type of Christmas tree
- `location`: Where the tree is located
- `height_m`: Height of the tree in meters

Additional columns are optional and will be preserved in the data.

## Sample Dataset

A sample dataset is included in `data/christmas_trees.csv` with 20 Christmas trees across different species and locations.

## Development

### Running Tests

```bash
# Using Poetry
poetry run pytest

# Or activate the shell first
poetry shell
pytest
```

### Project Structure

```
christmas-tree-counting/
├── christmas_tree_counting/    # Main package directory
│   ├── __init__.py            # Package initialization
│   ├── counter.py             # Core counting logic
│   └── cli.py                 # Command-line interface
├── data/                       # Sample datasets
│   └── christmas_trees.csv    # Sample tree data
├── tests/                      # Test files
├── pyproject.toml             # Poetry configuration
├── README.md                  # This file
└── .gitignore                 # Git ignore rules
```

## API Reference

### ChristmasTreeCounter

The main class for counting Christmas trees.

#### Methods

- `count_total_trees()` → `int`: Returns the total number of trees
- `count_by_species()` → `Dict[str, int]`: Returns counts grouped by species
- `count_by_location()` → `Dict[str, int]`: Returns counts grouped by location
- `count_by_height_range(min_height, max_height)` → `int`: Counts trees in height range
- `get_average_height()` → `float`: Calculates average tree height
- `get_summary()` → `Dict`: Returns comprehensive summary statistics

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

mpamey

## Acknowledgments

- Thanks to all Christmas tree enthusiasts! 🎄
- Built with Python and Poetry
