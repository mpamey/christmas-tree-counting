"""
Christmas Tree Counter Module

This module provides functionality to count Christmas trees from data files.
"""

import csv
from typing import Any, Dict, List, Optional
from pathlib import Path


class ChristmasTreeCounter:
    """
    A class for counting Christmas trees from data files.
    
    Attributes:
        data_file (Path): Path to the data file containing tree information.
        trees (List[Dict]): List of tree data loaded from the file.
    """
    
    def __init__(self, data_file: str):
        """
        Initialize the ChristmasTreeCounter.
        
        Args:
            data_file (str): Path to the CSV data file containing tree information.
        """
        self.data_file = Path(data_file)
        self.trees = []
        self._load_data()
    
    def _load_data(self) -> None:
        """Load tree data from the CSV file."""
        if not self.data_file.exists():
            raise FileNotFoundError(f"Data file not found: {self.data_file}")
        
        with open(self.data_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.trees = list(reader)
    
    def count_total_trees(self) -> int:
        """
        Count the total number of Christmas trees.
        
        Returns:
            int: Total number of trees in the dataset.
        """
        return len(self.trees)
    
    def count_by_species(self) -> Dict[str, int]:
        """
        Count trees grouped by species.
        
        Returns:
            Dict[str, int]: Dictionary with species as keys and counts as values.
        """
        species_count = {}
        for tree in self.trees:
            species = tree.get('species', 'Unknown')
            species_count[species] = species_count.get(species, 0) + 1
        return species_count
    
    def count_by_location(self) -> Dict[str, int]:
        """
        Count trees grouped by location.
        
        Returns:
            Dict[str, int]: Dictionary with locations as keys and counts as values.
        """
        location_count = {}
        for tree in self.trees:
            location = tree.get('location', 'Unknown')
            location_count[location] = location_count.get(location, 0) + 1
        return location_count
    
    def count_by_height_range(self, min_height: Optional[float] = None, 
                             max_height: Optional[float] = None) -> int:
        """
        Count trees within a specific height range.
        
        Args:
            min_height (Optional[float]): Minimum height in meters (inclusive).
            max_height (Optional[float]): Maximum height in meters (inclusive).
        
        Returns:
            int: Number of trees within the specified height range.
        """
        count = 0
        for tree in self.trees:
            try:
                height = float(tree.get('height_m', 0))
                if min_height is not None and height < min_height:
                    continue
                if max_height is not None and height > max_height:
                    continue
                count += 1
            except (ValueError, TypeError):
                continue
        return count
    
    def get_average_height(self) -> float:
        """
        Calculate the average height of all trees.
        
        Returns:
            float: Average height in meters, or 0 if no valid heights found.
        """
        heights = []
        for tree in self.trees:
            try:
                height = float(tree.get('height_m', 0))
                if height > 0:
                    heights.append(height)
            except (ValueError, TypeError):
                continue
        
        return sum(heights) / len(heights) if heights else 0.0
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get a comprehensive summary of the tree data.
        
        Returns:
            Dict: Summary statistics including counts, species, and averages.
        """
        return {
            'total_trees': self.count_total_trees(),
            'by_species': self.count_by_species(),
            'by_location': self.count_by_location(),
            'average_height_m': round(self.get_average_height(), 2)
        }
