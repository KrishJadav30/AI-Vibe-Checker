# Import the pipeline tool from the transformers library
from transformers import pipeline

print("Loading AI model... (This might take a few seconds the first time!)")

# 1. Initialize the AI. 
# The "sentiment-analysis" pipeline automatically downloads a pre-trained model.
vibe_checker = pipeline("sentiment-analysis")

print("\n--- AI Vibe Checker Ready ---")
print("Type 'quit' to exit.")

# 2. Create a loop so we can keep talking to it
while True:
    # Get text input from the user
    user_input = input("\nEnter a sentence: ")
    
    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
        
    # 3. Ask the AI to analyze the text
    result = vibe_checker(user_input)
    
    # 4. Extract the label (POSITIVE/NEGATIVE) and the confidence score
    sentiment = result[0]['label']
    confidence = result[0]['score'] * 100
    
    # 5. Print the results
    print(f"Result: {sentiment} (I am {confidence:.1f}% sure!)")