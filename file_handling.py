#1 Exploring Python's OS Module
#Task 1. Directory Inspector:
import os
import re
from collections import defaultdict
    
def list_dictionary_contents(path):
    try:
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The provided path '{path}' is not a directory.")
        
        with os.scandir(path) as entries:
            for entry in entries:
                entry_type = "Directory" if entry.is_dir() else "File"
                print(f"{entry.name} - {entry_type}")
    
    except FileNotFoundError:
        print(f"The provided path '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the path '{path}'.")
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")



#Task 2 File Size Reporter:
def report_file_sizes(directory):
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The provided path '{directory}' is not a directory.")
        
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    file_size = os.path.getsize(entry.path)
                    print(f"File: {entry.name} - Size: {file_size} bytes")
                else:
                    print(f"{entry.name} is not a file, skipping.")

    except FileNotFoundError:
        print(f"The provided path '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the path '{directory}'.")
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

#Task 3. File Extension Counter
def count_file_extenstions(directory):
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The provided path '{directory}' is not a directory.")
        
        extension_counts = defaultdict(int)

        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    _, ext = os.path.splitext(entry.name)
                    ext = ext.lower()
                    extension_counts[ext] += 1
        for ext, count in extension_counts.items():
            print(f"{ext.upper()}: {count}")

    except FileNotFoundError:
        print(f"The provided path '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the path '{directory}'.")
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}") 

#2 Regex-Powered Text Data Processing
#Task 1 Email Extractor:
def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
    
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

        emails = re.findall(email_pattern, content)

        unique_emails = set(emails)

        print("Extracted email addresses: ")
        for email in unique_emails:
            print(email)

        return list(unique_emails)
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

#3 Advanced Python Data Processing and Analysis Challenge
#Task 1 Travel Blog Sentiment Analysis:
import re

# Define positive and negative words
positive_words = ["amazing", "enjoy", "beautiful", "wonderful", "breathtaking", "relaxed", "soaked", "excellent", "delicious", "enlightening", "fantastic", "memorable", "stunning", "unique"]
negative_words = ["bad", "disappointing", "poor", "lackluster", "scarce", "overcrowded", "rain", "guide", "accommodations"]

def count_sentiment_words(text, words):
    """Count occurrences of each word in the text."""
    word_counts = {word: len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE)) for word in words}
    return word_counts

def extract_and_analyze_sentiment(filename):
    try:
        # Read the contents of the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count positive and negative words
        positive_counts = count_sentiment_words(content, positive_words)
        negative_counts = count_sentiment_words(content, negative_words)
        
        # Summarize the results
        total_positive = sum(positive_counts.values())
        total_negative = sum(negative_counts.values())

        print("Sentiment Analysis Report")
        print("------------------------")
        print("Positive words count:")
        for word, count in positive_counts.items():
            if count > 0:
                print(f"{word}: {count}")
        print("\nNegative words count:")
        for word, count in negative_counts.items():
            if count > 0:
                print(f"{word}: {count}")
        
        print("\nSummary:")
        print(f"Total positive words: {total_positive}")
        print(f"Total negative words: {total_negative}")
        
        return total_positive, total_negative
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    #1
    directory_path = input("Please enter the directory path: ")
    list_dictionary_contents(directory_path)
    report_file_sizes(directory_path)
    count_file_extenstions(directory_path)
    #2
    filename = "contacts.txt"
    extract_emails(filename)
    #3
    filename = "travel_blogs.txt"  # Change this to the path of your file if needed
    extract_and_analyze_sentiment(filename)


