
# Language Translator App

## Description
This is a simple web application that translates text from one language to another using the Google Translate API. The app provides an easy-to-use interface and supports translation to multiple languages.

---

## Project Structure
```
LanguageTranslator/
│
├── templates/
│   └── index.html          # HTML file for the app's interface
│
├── static/
│   └── style.css           # CSS file for styling
│
├── app.py                  # Main Flask application
│
└── README.md               # Documentation file
```

---

## Setup Instructions

### 1. Install Python
Download and install Python from [python.org](https://www.python.org/). Ensure that you add Python to your system's PATH during installation.

### 2. Clone the Repository
Clone this project to your local machine:
```bash
git clone <repository_url>
cd LanguageTranslator
```

### 3. Install Required Libraries
Use `pip` to install the required dependencies:
```bash
pip install flask googletrans==4.0.0-rc1
```

### 4. Run the Application
Open a terminal in the project directory and run:
```bash
python app.py
```

### 5. Access the Application
Open your web browser and go to:
```
http://127.0.0.1:5000
```

---

## Usage
1. Open the app in your web browser.
2. Enter the text you want to translate.
3. Select the target language from the dropdown menu.
4. Click the "Translate" button to view the translated text.

---

## Features
- **Simple Interface**: A clean and user-friendly design for inputting text and selecting languages.
- **Multiple Language Support**: Translate text into Spanish, French, and German. Adding more languages is straightforward.
- **Real-time Translation**: Displays translated text instantly.

---

## Future Enhancements
- **Add More Languages**: Extend the list of supported languages in the dropdown menu.
- **User Authentication**: Allow users to log in and save their translation history.
- **Improved UI/UX**: Enhance the design using advanced HTML/CSS and JavaScript features.

---

## Dependencies
- **Flask**: A lightweight WSGI web application framework.
- **Googletrans**: A Python library for integrating with Google Translate.

Install dependencies via:
```bash
pip install flask googletrans==4.0.0-rc1
```

---

## License
This project is licensed under the **MIT License**.

---

Feel free to contribute by submitting issues or pull requests. Feedback is always welcome!
