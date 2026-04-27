import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
        print(f"Execution time: {self.interval:.4f} seconds")

def optimized_function(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    return result

def bulk_process(data):
    unique_data = set(data)
    results = [optimized_function([item]) for item in unique_data]
    return results

if __name__ == '__main__':
    data = [1, 2, 2, 3, 4, 4, 5]
    with Timer():
        print(bulk_process(data))
