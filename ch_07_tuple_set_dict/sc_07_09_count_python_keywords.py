# file: sc_07_09_count_python_keywords.py
from collections import Counter
from pathlib import Path

KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
}
 

def main() -> None:
  
    filename = input('Enter Python file name in cwd: ').strip()
    path = Path(filename)
    if not path.is_file():
        print(f'File not found: {path}')
        return
    try:
        text = path.read_text().split()
    except Exception as e:
        print(f'Error reading file: {e}')
        return

    list_of_all_keywords_in_file = [word for word in text if word in KEYWORDS]
     # Counter lager et dictionary-lignende objekt som teller forekomster
    result = Counter(list_of_all_keywords_in_file)
    for keyword, cnt in result.items():
        print(f"{keyword:10} {cnt}")


if __name__ == '__main__':
    main()
