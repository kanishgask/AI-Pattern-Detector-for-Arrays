import analyzer

def run_tests():
    test_arrays = [
        [100, 4, 200, 1, 3, 2],
        [1, 2, 0, 1],
        [10, 5, 6, 7, 1],
    ]

    for arr in test_arrays:
        print("\nTesting:", arr)
        result = analyzer.analyze_array(arr)
        print(result)

if __name__ == "__main__":
    run_tests()
