# Project---Keylogger

# Description:
This repository contains a simple yet effective keystroke logger implemented using the Python pynput library. It captures and logs every key press and release event on the keyboard, providing a basic framework for understanding how keystroke logging works. This project is intended for educational purposes and security research to demonstrate the fundamentals of capturing keyboard input programmatically.

# Project Explanation:
The keystroke logger utilizes the pynput library, which allows for monitoring and controlling input devices in Python. The main components of this project include:

1.Key Press Detection:

The press_key function is triggered whenever a key is pressed. It captures the key and appends it to a list, then calls the save_to_file function to log the key press to a file. It distinguishes between alphanumeric and special keys, printing a corresponding message for each.
2.Key Release Detection:

The release_key function is triggered whenever a key is released. It prints a message indicating which key was released. If the Escape key (Key.esc) is released, the listener stops, effectively ending the logging session.
3.File Writing:

The save_to_file function writes the captured keystrokes to a file named key_log.txt. Each key is converted to a string and spaces are added for readability.
4.Listener Setup:

The Listener class from pynput is used to monitor key press and release events. The listener runs in a loop, calling the appropriate functions for each event.


# Disclaimer:
This keystroke logging project is created for educational and security research purposes only. It is intended to demonstrate how keylogging works and to help users understand the potential security implications. Unauthorized use of this code to capture keystrokes on any system without permission is illegal and unethical. Use this code responsibly and ensure that you have explicit consent from the owner of the system on which you are running this keylogger.

# Contribution:
Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue. Please adhere to the code of conduct in all interactions.

# License:
This project is licensed under the MIT License. See the LICENSE file for more details.

