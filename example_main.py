import sys
# check this for more on sys module: https://realpython.com/ref/stdlib/sys/

def greet(name):
    """Print a greeting."""
    return f"Hello, {name}"


def main():
    """Entry point when the file is run as a script."""
    if len(sys.argv) != 2:
        print("Usage: python example_main.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(greet(name))


# Runs only when executed directly, not on import
if __name__ == "__main__":
    main()
