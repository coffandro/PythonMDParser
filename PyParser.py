import argparse
import sys


def directory(raw_path):
    if not os.path.isdir(raw_path):
        raise argparse.ArgumentTypeError(
            '"{}" is not an existing directory'.format(raw_path)
        )
    return os.path.abspath(raw_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A markdown to html parser by Coffandro"
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        metavar="",
        type=argparse.FileType("r"),
        help="Path to the input MD file",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        metavar="",
        type=argparse.FileType("r"),
        help="Path to the output html file",
    )
    parser.add_argument(
        "--header",
        required=False,
        metavar="",
        type=argparse.FileType("r"),
        help="Path to a header file, this will be placed in the output before the content",
    )
    parser.add_argument(
        "--footer",
        required=False,
        metavar="",
        type=argparse.FileType("r"),
        help="Path to a footer file, this will be placed in the after before the content",
    )
    args = parser.parse_args()

    output = ""
    header = ""
    footer = ""

    if args.output:
        output = args.output.name
    if args.header:
        header = args.header.name
    if args.footer:
        footer = args.footer.name
    if args.input:
        print(output, header, footer)
