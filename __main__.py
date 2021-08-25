import argparse
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

    parser.start()

    token_text_list = []

    if parser._syntaxErrors == 0:
        print([LCCLexer.ruleNames[token.type - 1] for token in parser.getTokenStream().tokens])

        for token in parser.getTokenStream().tokens:
            if token.type == 34:
                if token.text not in token_text_list:
                    token_text_list.append(token.text)
                    print("IDENT '{}' na linha {} coluna {}".format(token.text, token.line, token.column))


if __name__ == '__main__':
    main()
