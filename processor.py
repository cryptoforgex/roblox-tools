import time

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        start_time = time.time()
        self._optimize_data()
        print(f"Processing completed in {time.time() - start_time:.4f} seconds")

    def _optimize_data(self):
        self.data = sorted(set(self.data))  # Remove duplicates and sort
        self.data = self._filter_data(self.data)

    def _filter_data(self, data):
        return [item for item in data if self._is_valid(item)]

    def _is_valid(self, item):
        return isinstance(item, int) and item > 0

if __name__ == '__main__':
    data = [5, 3, 8, 3, 2, -1, 7, 5]
    processor = DataProcessor(data)
    processor.process_data()