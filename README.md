# BookBot: Novel Static Analysis Tool
 -BookBot was one of my first project!

This repository contains a Python script that performs static analysis on text files, specifically novels like *Frankenstein*. The script will provide two types of analysis:

1. **Word Count**: It calculates the total number of words in the novel.
2. **Character Frequency**: It counts how many times each alphabetical character (A-Z) appears in the novel. Example: "The 'x' character was found 'y' times."

This project was created in collaboration with **[Boot.Dev](https://boot.dev)**.

## Features

- **Word Counting**: The script computes the total number of words in a text file.
- **Character Frequency**: It analyzes the frequency of each alphabetic character (ignoring case).

## How to Use

### Prerequisites
Make sure you have Python installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### Steps

1. **Set the Path to Your Novel**:  
   - Ensure that you have the text file of the novel (e.g., `frankenstein.txt`) saved on your computer.
   - Update the `book_path` variable in `main.py` to the path of your novel's text file on your computer. Example:
     ```python
     book_path = "/path/to/your/frankenstein.txt"
     ```

2. **Run the Script**:  
   Once the path is set, run the main script:
   ```bash
   python main.py
   ```
3. **View the Results**:  
   After running the script, you'll see:
       The total number of words in the novel.
       The frequency of each alphabetical character (A-Z).

**Example Output**:
    ```bash
    Total words in the novel: 78,456
    The 'a' character was found 4,332 times.
    The 'b' character was found 1,234 times.
    The 'c' character was found 2,345 times.
    ```

**Contributing**:
    Feel free to open issues or submit pull requests if you want to contribute or suggest new features. Contributions are always welcome!