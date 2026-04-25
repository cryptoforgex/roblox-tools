import time

class PerformanceTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()
        return self.end_time - self.start_time

    def get_elapsed_time(self):
        return self.end_time - self.start_time if self.start_time is not None and self.end_time is not None else None

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self):
        return [item for item in self.data if item['active']]

    def process_data(self):
        tracker = PerformanceTracker()
        tracker.start()
        filtered = self.filter_data()
        processed = self._enhance_data(filtered)
        elapsed = tracker.stop()
        print(f"Processing time: {elapsed:.4f} seconds")
        return processed

    def _enhance_data(self, data):
        return [{**item, 'enhanced': True} for item in data]

# Sample usage
if __name__ == '__main__':
    data = [{'active': True}, {'active': False}, {'active': True}]
    processor = DataProcessor(data)
    result = processor.process_data()
    print(result)