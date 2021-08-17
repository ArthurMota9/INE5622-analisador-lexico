import argparse
from os import path
from antlr4 import FileStream, CommonTokenStream

from LCCLexer import LCCLexer
from LCCParser import LCCParser

def main():
    # Argument parser
    parser_args = argparse.ArgumentParser(prog='LCC', description='LCC interpreter')
    parser_args.add_argument('input', type=str, help='source code')
    args = parser_args.parse_args()

    input_stream = FileStream(args.input)

    lexer = LCCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LCCParser(stream)

    tree = parser.start()

if __name__ == '__main__':
    main()