import analyzer
import explainer

def run():
    print("=== AI Array Pattern Detector ===")
    arr = list(map(int, input("Enter numbers: ").split()))

    result = analyzer.analyze_array(arr)
    explanation = explainer.generate_explanation(result)

    print("\n--- RESULTS ---")
    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n--- AI EXPLANATION ---")
    print(explanation)

if __name__ == "__main__":
    run()
