"""
Command-line interface for Christmas Tree Counting.
"""

import sys
import json
from pathlib import Path
from .counter import ChristmasTreeCounter


def main():
    """Main CLI entry point for counting Christmas trees."""
    if len(sys.argv) < 2:
        print("Usage: count-trees <data_file.csv>")
        print("\nExample: count-trees data/christmas_trees.csv")
        sys.exit(1)
    
    data_file = sys.argv[1]
    
    try:
        counter = ChristmasTreeCounter(data_file)
        summary = counter.get_summary()
        
        print("=" * 50)
        print("Christmas Tree Counting Summary")
        print("=" * 50)
        print(f"\nTotal Trees: {summary['total_trees']}")
        
        print(f"\nAverage Height: {summary['average_height_m']} meters")
        
        print("\nTrees by Species:")
        for species, count in summary['by_species'].items():
            print(f"  - {species}: {count}")
        
        print("\nTrees by Location:")
        for location, count in summary['by_location'].items():
            print(f"  - {location}: {count}")
        
        print("=" * 50)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
