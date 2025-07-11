from collections import Counter

def get_book_text(filename):
    with open(filename, 'r') as file:
        return file.read()

def get_book_length(filename):
    with open(filename, 'r') as file:
        return len(file.read().split()) 
    
def get_character_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    filtered_text = ''.join(c.lower() for c in text if c.isalpha())  # Convert to lowercase and filter non-alphabetic characters
    freq = sorted(Counter(filtered_text).items(), key=lambda x: x[1], reverse=True) # Sort by frequency in descending order

    return freq