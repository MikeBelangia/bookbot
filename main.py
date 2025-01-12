import string

bookpath = "./books/frankenstein.txt"

def main():
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents

def count(book_contents):
    words = book_contents.split()
    return len(words)

def character_frequency(book_contents):
    letter_counts = {}
    for l in string.ascii_lowercase:
        letter_counts[l] = 0
        
    for letter in book_contents:
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1

    return(letter_counts)

def sort_results(count_dict):
    results = []
    for count in count_dict:
        results.append((count_dict[count],count))
    results.sort(reverse=True)
    return(results)

    
text = main()    
word_count = count(text)
letter_freq = character_frequency(text)
final_results = sort_results(letter_freq)

print(f"--- Begin report of {bookpath} ---")
print(f"{word_count} words found in the document")
print("")
for result in final_results:
    print(f"The '{result[1]}' character was found {result[0]} times")
#print(f"--- End report ---")