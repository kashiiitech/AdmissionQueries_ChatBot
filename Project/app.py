from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Initialize NLTK and spaCy
import nltk
import spacy
from nltk.tokenize import word_tokenize
from spacy.matcher import Matcher

nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

from admission_rules import admissions_rules  # Import the dictionary

def get_response(user_input):
    user_input = user_input.lower()
    response = None
    
    # Use spaCy for named entity recognition
    doc = nlp(user_input)
    entities = [ent.text for ent in doc.ents]
    
    # Use NLTK for tokenization
    tokens = word_tokenize(user_input)
    
    # Initialize the Matcher
    matcher = Matcher(nlp.vocab)
    
    # Define pattern for asking for help
    help_pattern = [{"LOWER": "help"}]
    matcher.add("HelpPattern", [help_pattern])
    
    # Match the patterns
    matches = matcher(doc)
    
    # Check if the user is asking for help
    if matches:
        response = "Sure, I'm here to help! How can I assist you?"
    else:
        # Check each rule and respond accordingly
        for intent, data in admissions_rules.items():
            for pattern in data.get("patterns", []):
                if any(token in tokens for token in word_tokenize(pattern)):
                    response = data["responses"][0]
                    break
    
    # If no matching rule, use the default response
    if response is None:
        response = admissions_rules["default"]["responses"][0]
    
    return response

# Define route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    chatbot_response = ''
    
    if request.method == 'POST':
        user_input = request.form['user_input']
        chatbot_response = get_response(user_input)
        return jsonify({'response': chatbot_response})
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
