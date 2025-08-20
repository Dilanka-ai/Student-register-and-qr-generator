# 👨‍🎓 Student Data Management System with QR Code Generation

A simple command-line application in Python for managing student data. The system allows you to enter a student's name, address, age, and grade, and then automatically saves this information to a text file. For each student, it also generates a unique QR code that encodes the file path to their saved data.

## ✨ Features

* **Student Data Input**: A user-friendly interface to input a student's name, address, age, and grade.
* **File Storage**: Automatically saves each student's information into a dedicated `.txt` file.
* **Unique QR Code Generation**: Creates a unique QR code for each student that contains a string with their name and the file path to their data.
* **Organized File Structure**: Automatically creates a `students` directory to store both the text files and the QR code images.

## ⚙️ How It Works

1.  **Input**: The `main.py` script starts the application and prompts the user to enter student details.
2.  **Data Processing**: The `Student` class in `student.py` handles the input, saving the information to a text file.
3.  **QR Code Generation**: The `qr_generator.py` module, which is called by `student.py`, uses the `qrcode` library to create a QR code image. The QR code contains the student's name and the path to their data file.
4.  **Output**: The system prints a confirmation message indicating that the student data and QR code have been successfully saved.

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* `qrcode` library. You can install it using pip:
    ```bash
    pip install qrcode
    ```

### Running the Application

1.  Clone this repository to your local machine.
2.  Open your terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the main script:
    ```bash
    python main.py
    ```
5.  Follow the on-screen prompts to add student data. The application will continue to ask if you want to add more students until you enter 'n'.

## 📂 Project Structure

* `main.py`: The entry point of the application. It contains the main loop for adding students.
* `student.py`: Defines the `Student` class, which handles data input, file saving, and QR code path generation.
* `qr_generator.py`: Defines the `QRGenerator` class, which is responsible for creating the QR code image from a given text string.
* `students/`: A directory that is automatically created to store the student text files and QR code images.

## 🤝 Contribution

Feel free to fork this repository and contribute. Any improvements, bug fixes, or new features are welcome!

## 📄 License

This project is open-source and available under the MIT License.
