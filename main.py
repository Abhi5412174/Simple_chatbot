# Simple chatbot using basic pattern matching
from datetime import datetime
import re

response_dict = {
    r"\b(hi|hello|hey)\b": "Hello! How can I assist you today?",
    r"\b(name|who are you)\b": "I am a simple chatbot created to assist you with basic tasks!",
    r"\b(time|date)\b": "I don't have a watch, but I can get the current time for you! ",
    r"\b(how are you|what's up)\b": "I'm just a chatbot, but I'm functioning well! How about you?",
    r"\b(help|assist)\b": "I'm here to assist you with basic questions. What do you need help with?",
    r"\b(weather|temperature)\b": "I can provide weather info if I were connected to the internet.",
    r"\b(thanks|thank you)\b": "You're welcome! Let me know if you need more help.",
    r"\b(goodbye|bye)\b": "Goodbye! Have a great day ahead!",
    r"\b(joke|funny)\b": "Why don't programmers like nature? It has too many bugs!",
    r"\b(food|hungry)\b": "I'm a chatbot, so I don't eat, but I can suggest some recipes!",
    r"\b(movie|film)\b": "I heard 'The Greatest of All Time' featuring Thalapathy Vijay is a popular one!",
    r"\b(weather|weather today)\b": "Its great wearher today! You should go outside for relax!",
    r"\b(good|great)\b": "Nice to hear about that."
}

for i in range(1, 101):
    response_dict[fr"\b(topic{i})\b"] = f"Response for topic {i}"

def chatbot_response(user_input):
    user_input = user_input.lower()

    for pattern, response in response_dict.items():
        if re.search(pattern, user_input):
            if pattern == r"\b(time|date)\b":
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
                return response + current_datetime
            return response

    return "Sorry, I don't understand. Can you please clarify?"

def main():
    print("Chatbot: Hi! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
