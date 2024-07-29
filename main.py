def main():
    path = "./books/frankenstein.txt"
    text = get_file_text(path)
    character_dict = count_characters(text)
    count = get_words_count(text)
    print_report(path, character_dict, count)

def print_report(path, character_dict, character_count):
    print(f"--- Begin report on {path} ---")
    print(f"{character_count} words found in the document \n")

    def sort_on(dict):
        return dict["num"]

    list_of_characters = []
    for entry in character_dict:
        obj = {
            "character": entry,
            "num": character_dict[entry]
        }

        list_of_characters.append(obj)

    list_of_characters.sort(reverse=True, key=sort_on)

    for character_obj in list_of_characters:
        if not character_obj["character"].isalpha():
            continue
        print(f"The '{character_obj['character']}' character was found {character_obj["num"]} times")

    print("--- End report ---")

def get_words_count(text):
    words = text.split(" ")
    return len(words)

def get_file_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    character_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in character_dict:
            character_dict[lower_char] += 1
        else:
            character_dict[lower_char] = 1
    return character_dict

main()

