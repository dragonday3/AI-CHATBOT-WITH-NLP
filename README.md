# AI-CHATBOT-WITH-NLP

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: KAIRAVI SHAH

**INTERN ID**: CT12GAN

**DOMAIN**: PYTHON PROGRAMMING

**BATCH DURATION**: December 25th, 2024 to February 25th, 2025

**MENTOR NAME**: NEELA SANTHOSH

# **BotBuddy: AI Chatbot with NLP**

**BotBuddy** implements a simple yet effective chatbot using the Flask web framework and the Natural Language Toolkit (NLTK) for natural language processing. The chatbot is designed to engage users in conversation, answer questions, and provide information based on predefined patterns. It serves as a foundational example of how to create a web-based chatbot application, making it an excellent resource for those interested in natural language processing and web development.

**FILES INCLUDED IN THE REPO:**
- static (folder containing CSS and JavaScript file)
  - styles.css (CSS File)
  - script.js (JavaScript File)
- app.py (Main Python File)
- index.html (HTML File)

**KEY FEATURES:**
1. **Flask Web Framework**: The application is built using Flask, a lightweight and easy-to-use web framework for Python. Flask allows for quick development and deployment of web applications, making it an ideal choice for this project.

2. **Natural Language Processing with NLTK**: The chatbot utilizes NLTK, a powerful library for working with human language data. NLTK provides tools for tokenization, parsing, classification, and more, enabling the chatbot to understand and respond to user inputs effectively.

3. **Pattern Matching**: The chatbot employs a set of predefined patterns and responses, allowing it to recognize user inputs and generate appropriate replies. This pattern-matching approach is straightforward and effective for handling common queries.

4. **User-Friendly Interface**: The project includes a simple HTML frontend that allows users to interact with the chatbot easily. The interface features a chat box for displaying messages, an input field for user queries, and a send button for submitting messages.

5. **Responsive Design**: The chatbot interface is styled using CSS to ensure a clean and user-friendly experience. The design is responsive, making it accessible on various devices.

6. **JavaScript for Interactivity**: The frontend is enhanced with JavaScript, which handles user input and communicates with the Flask backend. This allows for real-time interaction, where users can send messages and receive responses without refreshing the page.

**HOW IT WORKS:**
The chatbot operates by matching user inputs against a set of predefined regex patterns. When a user sends a message, the Flask application receives the input and passes it to the NLTK chatbot. The chatbot processes the input, searches for a matching pattern, and generates a response based on the corresponding reply. The response is then sent back to the frontend, where it is displayed in the chat box.

**Code Structure:**
- **app.py**: This is the main Python script that sets up the Flask application, defines the chatbot logic, and handles incoming requests.
- **index.html**: The HTML file that serves as the user interface for the chatbot. It includes the structure for the chat box and input field.
- **static/styles.css**: The CSS file that styles the chatbot interface, ensuring a visually appealing layout.
- **static/script.js**: The JavaScript file that manages user interactions, sending messages to the backend and updating the chat box with responses.

**TOOLS/TECH. USED:**
- **Python**: The primary programming language used for developing the application, enabling the implementation of backend logic and natural language processing.
- **Flask**: A lightweight web framework for Python that facilitates the creation of web applications. It handles routing, request processing, and serves the frontend interface.
- **NLTK (Natural Language Toolkit)**: A powerful library for natural language processing in Python. It provides tools for working with human language data, including tokenization, parsing, and pattern matching.
- **HTML**: The markup language used to create the structure of the chatbot's user interface, allowing users to interact with the chatbot through a web browser.
- **CSS**: A stylesheet language used to style the HTML elements of the chatbot interface, ensuring a visually appealing and user-friendly design.
- **JavaScript**: A programming language used to add interactivity to the web application. It handles user input, sends messages to the Flask backend, and updates the chat box with responses in real-time.
- **Regex (Regular Expressions)**: A sequence of characters used for pattern matching in user inputs, allowing the chatbot to identify and respond to various queries effectively.
- **JSON**: A lightweight data interchange format used for sending and receiving data between the frontend and backend, particularly for the chat messages.

**INSTALLATION AND USAGE:**
