# Route Comparator

This repository contains a Python script for comparing two route tables and identifying routes present in one table that are missing from the other. This can be particularly useful for network engineers and administrators who must compare two routing tables and find missing routes.

## Features

- Compares two routing tables from text files.
- Identifies and lists routes missing from the first table but present in the second.
- Easy to use with command-line inputs for file names.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/route-comparator.git
    cd route-comparator
    ```

2. Prepare your route tables in text files. Ensure each route entry is on a separate line.

3. Run the script:
    ```bash
    python3 route-compare.py
    ```

4. Follow the prompts to enter the file names for your SD-WAN and WAN distribution route tables.

## Example

Assuming your route tables are saved as `table-1.txt` and `table-2.txt`, running the script will prompt you to input these file names. The script will then output the routes that are present in the 2nd table but missing from the 1st table.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the license file for details.

## Contact

For more information, please contact Patrick Teague (mailto:paddymack@gmail.com).