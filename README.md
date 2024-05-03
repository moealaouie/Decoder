# Message Decoder Program

## Description
This Python program decodes a message by reading a file containing lines with a number and a word. It extracts words based on a specific counting pattern, sorting them by their associated number, and then constructing a final message from these words. The script is intended for use with a specific formatted file named `message.txt`.

## Functionality
- **decode(file)**: This function reads the input file line by line. It only considers lines with exactly two elements separated by space (a number and a word). It collects these pairs into a list, sorts them by the numerical value, and then extracts every nth word following a cumulative counting pattern, where n starts at 1 and increments after each extraction.
- It creates a pyramid where the word associated with the last number on each level is printed:

```  
   1
  2 3
 4 5 6
7 8 9 10
```

The printed words would be the words associated with [1, 3, 6, 10]
## Requirements
- Python 3.x

## Setup and Execution
1. Ensure that Python 3.x is installed on your system.
2. Place the script and the `message.txt` file in the same directory.
3. Run the script using the command:
   `python script_name.py`

## Input File Format
The input file, `message.txt`, should contain lines formatted as follows:
```
1 hello
2 world
```

## Authors
- Mohamed Alaouie

## License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
