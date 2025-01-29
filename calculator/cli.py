# cli.py
import argparse
from calculator.calculator import add, subtract, multiply, divide  # Ensure correct import path

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help="Operation to perform")
    parser.add_argument('a', type=float, help="First number")
    parser.add_argument('b', type=float, help="Second number")
    
    args = parser.parse_args()

    if args.operation == 'add':
        result = add(args.a, args.b)
    elif args.operation == 'subtract':
        result = subtract(args.a, args.b)
    elif args.operation == 'multiply':
        result = multiply(args.a, args.b)
    elif args.operation == 'divide':
        result = divide(args.a, args.b)
    
    if result is not None:
        print(f"Result: {result}")
    else:
        print(f"Operation '{args.operation}' is not yet implemented.")

if __name__ == '__main__':
    main()
