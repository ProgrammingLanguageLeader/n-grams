import argparse


class Arguments:
    def __init__(self):
        self.parser: argparse.ArgumentParser = Arguments.create_argument_parser()
        args = self.parser.parse_args()
        self.source_file: str = args.source
        self.n_max: int = args.n_max
        self.verbosity: bool = args.verbose
        self.output_dir: str = args.output
        self.pretty_printing: bool = args.pretty

    @staticmethod
    def create_argument_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description='Calculates n-grams frequencies')
        parser.add_argument(
            'source',
            type=str,
            help='Path to the file with source text'
        )
        parser.add_argument(
            '-n', '--n_max',
            type=int,
            help='Maximum value of n for n-grams frequency calculation',
            default=8
        )
        parser.add_argument(
            '-v', '--verbose',
            action='store_true',
            help='Enables verbalisation',
            default=False,
        )
        parser.add_argument(
            '-o', '--output',
            type=str,
            help='Path to the directory where results should be stored',
            default='.'
        )
        parser.add_argument(
            '-p', '--pretty',
            action='store_true',
            help='Enables pretty printing of results',
            default=False
        )
        return parser
