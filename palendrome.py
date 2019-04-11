palendrome_list = []


def analyze(input_string):
    
    print(f"Your string is: {input_string} \nWith length: {len(input_string)}")
    
    for item in input_string:
        pass  
    pass


def main():
    
    while True:
        
        try:
            input_string = input(f'Enter string for analysis\n')
            
        except Exception as e:
            print(f"Please enter a valid string: {e}")

        else:
            analyze(input_string)
            print(f"\n")
            
if __name__ == '__main__':
    main()