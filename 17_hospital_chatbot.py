# Practical: Hospital Enquiry Chatbot (Rule-Based)


def hospital_chatbot():
  print("=" * 50)
  print("🏥 Welcome to City Care Hospital Enquiry Bot!")
  print("=" * 50)
  print("Type your questions below (Type 'bye' or 'exit' to end chat).\n")

  while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
      print("Bot: Hello! Welcome to City Care Hospital. How can I help you?")

    elif "appointment" in user_input or "book" in user_input:
      print(
          "Bot: To book an appointment, please provide the doctor's department"
          " or call our reception desk at 020-23456789."
      )

    elif "timing" in user_input or "hours" in user_input or "time" in user_input:
      print(
          "Bot: OPD timings are Monday to Saturday, 9:00 AM to 8:00 PM."
          " Emergency services are open 24/7."
      )

    elif "department" in user_input or "specialist" in user_input or "doctor" in user_input:
      print(
          "Bot: We have departments for Cardiology, Orthopedics, Pediatrics,"
          " Neurology, and General Medicine."
      )

    elif "emergency" in user_input or "ambulance" in user_input or "casualty" in user_input:
      print(
          "Bot: For immediate emergency or ambulance dispatch, please call our"
          " 24/7 helpline at 108 or 020-99998888."
      )

    elif "fees" in user_input or "charges" in user_input or "cost" in user_input:
      print(
          "Bot: General OPD consultation fee is ₹500. Specialist consultation"
          " fees range from ₹800 to ₹1500."
      )

    elif "location" in user_input or "address" in user_input:
      print(
          "Bot: Our hospital is located near Swargate, Pune, Maharashtra."
      )

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
      print(
          "Bot: Thank you for contacting City Care Hospital. Wishing you a"
          " speedy recovery! Goodbye!"
      )
      break

    else:
      print(
          "Bot: I'm sorry, I didn't quite catch that. You can ask me about"
          " appointments, timings, departments, emergency services, or fees."
      )


# Run the chatbot
hospital_chatbot()