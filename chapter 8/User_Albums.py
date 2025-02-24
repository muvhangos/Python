messages = ["Hello, how are you?", "Don't forget the meeting at 10 AM.", "Happy Birthday!", "See you soon!"]

# List to hold sent messages
sent_messages = []

def send_messages(messages, sent_messages):
    """
    Prints each message and moves it to the sent_messages list.
    """
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Call the function
send_messages(messages, sent_messages)

# Print both lists to verify the messages were moved correctly
print("\nOriginal messages list:")
print(messages)

print("\nSent messages list:")
print(sent_messages)