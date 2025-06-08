from stats import get_num_words, char_count, sort_char_count
import sys

def get_book_text(file_path):
    file_content = None
    with open(file_path) as f:
        file_content = f.read()
    if file_content is None:
        raise FileNotFoundError("File not found")
    return file_content

def make_header(line_char='-', text=""):
    header = ""
    for i in range(0, 13):
        header += line_char
    header += " "
    header += text
    header += " "
    for i in range(0, 34 - len(header)):
        header += line_char
    header += "\n"
    return header

def create_report(file_path, num_words, char_count_list):
    report = ""
    report += make_header(line_char='=', text="BOOKBOT")
    report += f"Analyzing book found at {file_path}...\n"
    report += make_header(line_char='-', text="Word Count")
    report += f"Found {num_words} total words.\n"
    report += make_header(line_char='-', text="Character Count")
    for char_dict in char_count_list:
        report += f"{char_dict['char']}: {char_dict['num']}\n"
    report += make_header(line_char='=', text="END")
    return report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    char_count_dict = char_count(book_text)
    sorted_char_count_list = sort_char_count(char_count_dict)

    report = create_report(book_text, num_words, sorted_char_count_list)
    print(report)


main()