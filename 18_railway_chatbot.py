# Practical: Railway Enquiry Chatbot (Rule-Based)


def railway_chatbot():
  print("=" * 50)
  print("🚂 Welcome to Indian Railways Enquiry Bot!")
  print("=" * 50)
  print("Type your questions below (Type 'bye' or 'exit' to end chat).\n")

  while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
      print("Bot: Hello! Welcome to Indian Railways enquiry service.")

    elif "train" in user_input or "schedule" in user_input or "timing" in user_input:
      print(
          "Bot: You can check train running status and timetables by entering"
          " the 5-digit train number."
      )

    elif "pnr" in user_input or "status" in user_input or "seat" in user_input:
      print(
          "Bot: To check your PNR status or seat confirmation, please provide"
          " your 10-digit PNR number."
      )

    elif "booking" in user_input or "book" in user_input or "ticket" in user_input:
      print(
          "Bot: Tickets can be booked online through the IRCTC portal or mobile"
          " application."
      )

    elif "platform" in user_input or "pf" in user_input:
      print(
          "Bot: Platform numbers are displayed on station electronic boards"
          " around 20 minutes before departure."
      )

    elif "cancellation" in user_input or "refund" in user_input:
      print(
          "Bot: Ticket cancellations and refunds can be processed directly through"
          " your IRCTC user account."
      )

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
      print(
          "Bot: Thank you for using Indian Railways enquiry. Have a safe"
          " journey! Goodbye!"
      )
      break

    else:
      print(
          "Bot: I'm sorry, I didn't quite catch that. You can ask me about train"
          " schedules, PNR status, ticket bookings, or platform details."
      )


# Run the chatbot
railway_chatbot()