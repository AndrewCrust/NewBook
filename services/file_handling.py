import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    stop = start + size

    if len(text[start : stop]) < size:
        return text[start:], len(text[start:])

    while True:
        if text[stop - 1] in '.,;:?!' and text[stop] not in '.!':
            return text[start: stop], stop - start
        stop -= 1


def prepare_book(path: str) -> None:

    with open(path, 'r',  encoding='utf-8') as f:
        text = f.read()
        start = 0
        count = 1
        while True:
            page, index = _get_part_text(text, start, PAGE_SIZE)
            if not index:
                break
            book[count] = page.lstrip()
            count += 1
            start += index



prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
