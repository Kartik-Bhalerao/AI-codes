# Practical: Banking Enquiry Chatbot (Rule-Based)


def banking_chatbot():
  print("=" * 50)
  print("🏦 Welcome to Apex Bank Customer Support Bot!")
  print("=" * 50)
  print("Type your questions below (Type 'bye' or 'exit' to end chat).\n")

  while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
      print("Bot: Hello! Welcome to Apex Bank. How can I assist you today?")

    elif "balance" in user_input or "account" in user_input:
      print(
          "Bot: You can securely check your account balance by logging into"
          " our mobile banking app or internet banking portal."
      )

    elif "loan" in user_input or "interest" in user_input:
      print(
          "Bot: We offer Home Loans, Car Loans, and Personal Loans at"
          " competitive interest rates starting at 8.5% p.a."
      )

    elif "card" in user_input or "atm" in user_input or "debit" in user_input:
      print(
          "Bot: For lost/stolen cards or ATM PIN generation, please use"
          " our mobile app or call our 24/7 card services helpline."
      )

    elif "branch" in user_input or "location" in user_input or "ifsc" in user_input:
      print(
          "Bot: Our main branch and ATM network is spread across Pune."
          " You can find specific branch IFSC codes on our official website."
      )

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
      print(
          "Bot: Thank you for banking with Apex Bank. Have a wonderful"
          " day! Goodbye!"
      )
      break

    else:
      print(
          "Bot: I'm sorry, I didn't quite catch that. You can ask about"
          " account balance, loans, cards, or branch locations."
      )


# Run the chatbot
banking_chatbot()