import argparse


def main():
    arg_parser = argparse.ArgumentParser()
    subparsers = arg_parser.add_subparsers(
        dest="command", required=True, help="the subcommand to run"
    )

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument(
        "file",
        type=argparse.FileType("r"),
        required=True,
        help="the brainfuck source code file to run",
    )
    run_parser.add_argument("mode", default="u8", choices=["u8", "u16", "inf"])

    args = arg_parser.parse_args()

    if args.command == "run":
        pass


if __name__ == "__main__":
    main()
