"""
main module for fbf
"""
import argparse
from .run import run_bf


def main():
    """
    main func to parse command line arguments
    """
    arg_parser = argparse.ArgumentParser()
    subparsers = arg_parser.add_subparsers(
        dest="command", required=True, help="the subcommand to run"
    )

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument(
        "file",
        type=argparse.FileType("r"),
        help="the brainfuck source code file to run",
    )
    run_parser.add_argument(
        "--mode",
        default="u8",
        choices=["u8", "u16", "inf"],
        help="set cell type,default is u8",
    )

    args = arg_parser.parse_args()

    if args.command == "run":
        run_bf(args.file, args.mode)


if __name__ == "__main__":
    main()
