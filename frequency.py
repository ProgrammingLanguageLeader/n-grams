import json
import logging
import os
import string
import time
from collections import defaultdict, OrderedDict
from typing import DefaultDict, Any, Dict, Callable

from arguments import Arguments


def benchmark_time(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        logger = logging.getLogger(__name__)
        start_time = time.time()
        call_result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f'time was spent: {end_time - start_time}')
        return call_result
    return wrapped_func


def config_logger(verbose: bool):
    logger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO if verbose else logging.WARN)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)


def load_file(path: str, encoding: str = 'utf-8') -> str:
    with open(path, encoding=encoding) as file:
        file_content = file.read()
    return file_content


def filter_text(text: str, alphabet: str) -> str:
    filtered_text = ''
    for line in text.splitlines():
        for char in line:
            lower_char = char.lower()
            if lower_char in '0123456789 ' or lower_char in alphabet:
                filtered_text += lower_char
            elif lower_char in string.punctuation:
                filtered_text += ' '
        filtered_text += ' '
    return ' '.join(filtered_text.split())


@benchmark_time
def calc_char_sequence_frequency(text: str, chars_number: int) -> DefaultDict[Any, int]:
    frequency = defaultdict(int)
    for char_index in range(len(text) - chars_number):
        char_seq = text[char_index:char_index + chars_number]
        frequency[char_seq] += 1
    return frequency


@benchmark_time
def dump_frequency_stats(
        frequency_stats: Dict[Any, int],
        file_path: str,
        encoding: str = 'utf-8',
        pretty: bool = False):
    indent = 4 if pretty else None
    ensure_ascii = False if pretty else None
    stats = OrderedDict(sorted(frequency_stats.items(), key=lambda item: -item[1])) if pretty else frequency_stats
    dirname = os.path.dirname(file_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(stats, file, indent=indent, ensure_ascii=ensure_ascii)


if __name__ == '__main__':
    args = Arguments()
    config_logger(args.verbosity)
    logger = logging.getLogger(__name__)
    text = load_file(args.source_file)
    filtered_text = filter_text(text, args.alphabet)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    for chars_number in range(1, args.n_max + 1):
        logger.info(f'Char sequence frequency calculation for n = {chars_number} was started')
        freq = calc_char_sequence_frequency(filtered_text, chars_number)
        logger.info(f'Char sequence frequency calculation for n = {chars_number} was competed')
        file_path = f'{args.output_dir}/{chars_number}-grams_frequency_stats.json'
        logger.info(f'Writing result to the file {file_path}')
        dump_frequency_stats(freq, file_path, pretty=args.pretty_printing)
