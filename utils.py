def parse_input(input_str):
    try:
        return list(map(int, input_str.split()))
    except:
        print("Invalid input!")
        return []
