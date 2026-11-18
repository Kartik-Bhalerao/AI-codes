# Practical: College Enquiry Chatbot (Rule-Based)


def college_chatbot():
  print("=" * 50)
  print("Welcome to College Enquiry Bot!")
  print("=" * 50)
  print("Type your questions below (Type 'bye' to exit).\n")

  while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
      print("Bot: Hello! Welcome to our college.")
    elif "admission" in user_input or "eligibility" in user_input:
      print("Bot: Admissions are open for B.E. Computer Engineering and IT.")
    elif "courses" in user_input or "branch" in user_input:
      print(
          "Bot: We offer B.E. in Computer Engineering, IT, Mechanical, and"
          " Civil."
      )
    elif "fees" in user_input:
      print("Bot: Please visit the administrative office for fee details.")
    elif "timing" in user_input:
      print("Bot: College working hours are 9:00 AM to 5:00 PM.")
    elif "location" in user_input or "address" in user_input:
      print("Bot: Our campus is located in Manjari, Pune.")
    elif "bye" in user_input or "exit" in user_input:
      print("Bot: Thank you! Goodbye!")
      break
    else:
      print("Bot: I didn't understand that. You can ask about admissions, courses, or fees.")


college_chatbot()