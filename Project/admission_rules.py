admissions_rules = {
  "admission_process": {
      "patterns": ["apply", "admission process", "application procedure"],
      "responses": [
          "To apply for admission, visit our website and fill out the online application form.",
          "The admission process involves submitting an online application form with your details and documents."
      ]
  },
  "application_deadline": {
      "patterns": ["deadline", "last date to apply"],
      "responses": [
          "The application deadline for this year's admissions is [specific date].",
          "You have until [specific date] to submit your application."
      ]
  },
  "required_documents": {
      "patterns": ["documents needed", "what to submit"],
      "responses": [
          "You'll need to submit your academic transcripts, letters of recommendation, a statement of purpose, and any other relevant documents.",
          "The required documents include academic records, letters of recommendation, a personal statement, and any additional materials specific to your program."
      ]
  },
  "eligibility_criteria": {
      "patterns": ["eligibility", "am I eligible to apply?"],
      "responses": [
          "Eligibility criteria vary depending on the program. Generally, a bachelor's degree in a related field is required.",
          "Eligibility criteria differ based on the program you're interested in. A bachelor's degree and certain prerequisites are commonly required."
      ]
  },
  "scholarships": {
      "patterns": ["scholarships available", "can I get a scholarship?"],
      "responses": [
          "Yes, we offer scholarships for outstanding students. You can find more information about available scholarships on our website.",
          "Scholarships are available for high-achieving students. Check our website for details on the types of scholarships and their requirements."
      ]
  },
  # Add more rules for other admission-related queries
  "default": {
      "responses": ["I'm sorry, I couldn't understand your query. Please rephrase or ask a different question."]
  }
}