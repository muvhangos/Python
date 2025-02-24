messages = ["Hello!", "How are you?", "Good morning!", "Have a great day!", "See you later!"]

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

def show_messages(messages):
    """
    Prints each text message in the list.
    """
    for message in messages:
        print(message)

# Call the function with a copy of the messages list
send_messages(messages[:], sent_messages)

# Print both lists to verify the original list retained its messages
print("\nOriginal messages list:")
print(messages)

print("\nSent messages list:")
print(sent_messages)