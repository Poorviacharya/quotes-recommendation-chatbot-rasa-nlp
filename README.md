# Quotes Recommendation Chatbot 🤖

This is a Flask + Rasa NLP chatbot that recommends quotes based on user mood.  
The frontend is served with Flask, and the backend NLP model is powered by Rasa.

## Features
- Motivational quotes
- Love quotes
- Funny quotes
- Success quotes

## Technologies Used
- Python
- Flask
- Rasa NLP
- HTML, CSS, JavaScript

## How to Run

1. Install dependencies:
 
  pip install rasa flask


2. Train the Rasa model:

rasa train


3. Run the Flask app:

python app.py


4. Open the frontend in browser:

http://127.0.0.1:8000


5. Make sure Rasa server is running for Flask to connect:

rasa run --enable-api --cors "*"


### Demo Video
[Watch the demo here](https://youtu.be/VNxvO4h86hw)


## Example Inputs
- "motivate me"
- "love quote"
- "funny quote"
- "success quote"

## Project Structure

rasa-quotes-chatbot/
├── app.py
├── index.html
├── data/
├── models/
├── config.yml
├── domain.yml
├── credentials.yml
├── endpoints.yml
└── README.md


## Future Enhancements
- Add more attractive frontend design with colors and CSS.  
- Save user chat history with login/session.  
- Add more quote categories.  
- Deploy on cloud server for public access.
