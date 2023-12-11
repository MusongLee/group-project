# Random Advice Generator

This Python script is a simple random advice generator that fetches advice from an external API, allows users to save advice to a file, and maintains a collection of saved advice. It is designed to be easy to use and integrate into other projects.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Usage

### 1. Fetch and Save Random Advice

- The script fetches a random piece of advice from the [Advice Slip API](https://api.adviceslip.com/advice).
- Users are prompted to save the advice to a file (`advice.txt`).
- The script records the date and time of the advice for reference.

### 2. Retrieve and Display Saved Advice

- The script can retrieve and display previously saved advice from the `advice.txt` file.
- Saved advice is displayed with a numbered format.

## Functions

- `fetch_random_advice()`: Fetches a random piece of advice from the API.
- `save_advice_to_file(advice, filename="advice.txt")`: Saves the provided advice to the specified file.
- `get_random_advice_from_file(filename="advice.txt")`: Retrieves saved advice from the specified file.
- `number_and_save_advice(advice_list, filename="advice.txt")`: Numbers and saves advice to the specified file.
- `yes_or_no()`: Asks the user if they want to save advice and returns a corresponding value.

## How to Run

1. Ensure you have Python installed.
2. Install the required `requests` library using `pip install requests`.
3. Run the script: `python script_name.py`.

## Example Output

- When fetching and saving a random piece of advice:

    ```plaintext
    Random Advice from API: Embrace the glorious mess that you are. (2023-12-12 15:30:45)

    Would you like to put this advice in advice.txt? ----- Press Y/N
    Y

    Save complete.
    ```

- When retrieving and displaying saved advice:

    ```plaintext
    Random Advice from advice.txt:
    1. Embrace the glorious mess that you are. (2023-12-12 15:30:45)

    Numbered Advice saved to advice.txt.
    ```

## Notes

- The script handles API errors and file read/write errors, displaying appropriate messages.
- The user can choose to save or skip saving advice when prompted.

Feel free to modify and adapt this script to suit your needs.
