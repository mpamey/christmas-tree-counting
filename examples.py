"""
Example usage of the Christmas Tree Counting package.

This script demonstrates how to use the package to count and analyze Christmas trees.
"""

from christmas_tree_counting import ChristmasTreeCounter


def main():
    # Initialize the counter with the sample dataset
    data_file = 'data/christmas_trees.csv'
    counter = ChristmasTreeCounter(data_file)
    
    print("🎄 Christmas Tree Counting Example 🎄\n")
    
    # Example 1: Count total trees
    total = counter.count_total_trees()
    print(f"📊 Total number of trees: {total}\n")
    
    # Example 2: Count by species
    print("🌲 Trees by species:")
    species_count = counter.count_by_species()
    for species, count in sorted(species_count.items(), key=lambda x: x[1], reverse=True):
        print(f"   {species}: {count} trees")
    print()
    
    # Example 3: Count by location
    print("📍 Trees by location:")
    location_count = counter.count_by_location()
    for location, count in sorted(location_count.items(), key=lambda x: x[1], reverse=True):
        print(f"   {location}: {count} trees")
    print()
    
    # Example 4: Filter by height
    small_trees = counter.count_by_height_range(max_height=2.5)
    medium_trees = counter.count_by_height_range(min_height=2.5, max_height=4.0)
    large_trees = counter.count_by_height_range(min_height=4.0)
    
    print("📏 Trees by size:")
    print(f"   Small (< 2.5m): {small_trees} trees")
    print(f"   Medium (2.5-4.0m): {medium_trees} trees")
    print(f"   Large (> 4.0m): {large_trees} trees")
    print()
    
    # Example 5: Average height
    avg_height = counter.get_average_height()
    print(f"📈 Average tree height: {avg_height:.2f} meters\n")
    
    # Example 6: Comprehensive summary
    print("📋 Complete Summary:")
    summary = counter.get_summary()
    print(f"   Total Trees: {summary['total_trees']}")
    print(f"   Average Height: {summary['average_height_m']}m")
    print(f"   Number of Species: {len(summary['by_species'])}")
    print(f"   Number of Locations: {len(summary['by_location'])}")


if __name__ == "__main__":
    main()
