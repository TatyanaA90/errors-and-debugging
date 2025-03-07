from syntax import syntax_errors
from runtime import runtime_errors
from logical import logical_errors

def main():
    syntax_errors()
    runtime_errors()
    logical_errors()

if __name__ == "__main__":
    main()
#print(f"debug: {main()}")