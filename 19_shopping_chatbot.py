# Practical: Online Shopping Assistant Chatbot (Rule-Based)


def shopping_chatbot():
  print("=" * 50)
  print("🛍️ Welcome to ShopEasy Assistant Bot!")
  print("=" * 50)
  print("Type your questions below (Type 'bye' or 'exit' to end chat).\n")

  while True:
    user_input = input("You: ").lower().strip()

    if "hello" in user_input or "hi" in user_input:
      print("Bot: Hello! Welcome to ShopEasy. How can I help you shop today?")

    elif "order" in user_input or "track" in user_input:
      print(
          "Bot: You can track your order status in real-time under the 'My"
          " Orders' section of your profile."
      )

    elif "return" in user_input or "refund" in user_input:
      print(
          "Bot: Returns and refunds can be initiated within 7 days of delivery"
          " via your order history page."
      )

    elif "shipping" in user_input or "delivery" in user_input:
      print(
          "Bot: Standard delivery takes 3 to 5 business days. Express shipping"
          " is available at checkout."
      )

    elif "payment" in user_input or "pay" in user_input:
      print(
          "Bot: We accept UPI, Credit/Debit cards, Net Banking, and Cash on"
          " Delivery (COD)."
      )

    elif "category" in user_input or "product" in user_input or "item" in user_input:
      print(
          "Bot: We offer various categories including Electronics, Fashion, Home"
          " Decor, and Groceries."
      )

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
      print(
          "Bot: Thank you for shopping with ShopEasy. Have a great day!"
          " Goodbye!"
      )
      break

    else:
      print(
          "Bot: I'm sorry, I didn't quite catch that. You can ask about order"
          " tracking, returns, shipping, or payment methods."
      )


# Run the chatbot
shopping_chatbot()