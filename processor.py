from typing import List, Dict

class DataProcessor:
    def __init__(self, data: List[Dict]) -> None:
        self.data = data

    def filter_data(self, threshold: int) -> List[Dict]:
        """
        Filters the data based on a threshold.

        Args:
            threshold (int): The threshold for filtering data.

        Returns:
            List[Dict]: A list of filtered data.
        """
        return [item for item in self.data if item.get('value', 0) > threshold]

    def aggregate_data(self) -> Dict[str, int]:
        """
        Aggregates the data to count occurrences of each type.

        Returns:
            Dict[str, int]: A dictionary with counts of each type.
        """
        aggregation = {} 
        for item in self.data:
            item_type = item.get('type', 'unknown')
            aggregation[item_type] = aggregation.get(item_type, 0) + 1
        return aggregation

    def sort_data(self) -> List[Dict]:
        """
        Sorts the data by the 'value' key in descending order.

        Returns:
            List[Dict]: A sorted list of data.
        """
        return sorted(self.data, key=lambda x: x.get('value', 0), reverse=True)