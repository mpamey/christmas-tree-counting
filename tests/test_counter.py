"""
Tests for the Christmas Tree Counter package.
"""

import pytest
from pathlib import Path
import tempfile
import csv
from christmas_tree_counting import ChristmasTreeCounter


@pytest.fixture
def sample_data_file():
    """Create a temporary CSV file with sample tree data."""
    data = [
        {'tree_id': '1', 'species': 'Norway Spruce', 'location': 'North Forest', 'height_m': '2.5', 'age_years': '5'},
        {'tree_id': '2', 'species': 'Douglas Fir', 'location': 'North Forest', 'height_m': '3.2', 'age_years': '7'},
        {'tree_id': '3', 'species': 'Fraser Fir', 'location': 'East Garden', 'height_m': '1.8', 'age_years': '3'},
        {'tree_id': '4', 'species': 'Norway Spruce', 'location': 'East Garden', 'height_m': '2.1', 'age_years': '4'},
        {'tree_id': '5', 'species': 'Douglas Fir', 'location': 'North Forest', 'height_m': '3.8', 'age_years': '8'},
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['tree_id', 'species', 'location', 'height_m', 'age_years'])
        writer.writeheader()
        writer.writerows(data)
        temp_path = f.name
    
    yield temp_path
    
    # Cleanup
    Path(temp_path).unlink()


def test_count_total_trees(sample_data_file):
    """Test counting total number of trees."""
    counter = ChristmasTreeCounter(sample_data_file)
    assert counter.count_total_trees() == 5


def test_count_by_species(sample_data_file):
    """Test counting trees by species."""
    counter = ChristmasTreeCounter(sample_data_file)
    species_count = counter.count_by_species()
    
    assert species_count['Norway Spruce'] == 2
    assert species_count['Douglas Fir'] == 2
    assert species_count['Fraser Fir'] == 1


def test_count_by_location(sample_data_file):
    """Test counting trees by location."""
    counter = ChristmasTreeCounter(sample_data_file)
    location_count = counter.count_by_location()
    
    assert location_count['North Forest'] == 3
    assert location_count['East Garden'] == 2


def test_count_by_height_range(sample_data_file):
    """Test counting trees within a height range."""
    counter = ChristmasTreeCounter(sample_data_file)
    
    # Count trees between 2 and 3 meters
    count = counter.count_by_height_range(min_height=2.0, max_height=3.0)
    assert count == 2  # Trees with heights 2.5 and 2.1
    
    # Count trees taller than 3 meters
    count = counter.count_by_height_range(min_height=3.0)
    assert count == 2  # Trees with heights 3.2 and 3.8


def test_get_average_height(sample_data_file):
    """Test calculating average tree height."""
    counter = ChristmasTreeCounter(sample_data_file)
    avg_height = counter.get_average_height()
    
    # Average of 2.5, 3.2, 1.8, 2.1, 3.8 = 13.4 / 5 = 2.68
    assert round(avg_height, 2) == 2.68


def test_get_summary(sample_data_file):
    """Test getting comprehensive summary."""
    counter = ChristmasTreeCounter(sample_data_file)
    summary = counter.get_summary()
    
    assert summary['total_trees'] == 5
    assert 'by_species' in summary
    assert 'by_location' in summary
    assert 'average_height_m' in summary
    assert summary['average_height_m'] == 2.68


def test_file_not_found():
    """Test error handling for missing file."""
    with pytest.raises(FileNotFoundError):
        ChristmasTreeCounter('nonexistent_file.csv')


def test_real_dataset():
    """Test with the actual dataset included in the package."""
    # This test assumes the data file exists in the expected location
    data_path = Path(__file__).parent.parent / 'data' / 'christmas_trees.csv'
    
    if data_path.exists():
        counter = ChristmasTreeCounter(str(data_path))
        assert counter.count_total_trees() == 20
        
        # Check species counts
        species_count = counter.count_by_species()
        assert 'Norway Spruce' in species_count
        assert 'Douglas Fir' in species_count
        
        # Check locations
        location_count = counter.count_by_location()
        assert len(location_count) > 0
