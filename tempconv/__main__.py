"""Command-line entry point: python -m tempconv 100 --from C --to F"""
import argparse
import sys

from tempconv.core import BelowAbsoluteZeroError, convert


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="tempconv", description="Convert temperatures between C, F and K.")
    parser.add_argument("value", type=float, help="temperature to convert")
    parser.add_argument("--from", dest="src", default="C", choices=["C", "F", "K"], help="source unit")
    parser.add_argument("--to", dest="dst", default="F", choices=["C", "F", "K"], help="target unit")
    args = parser.parse_args(argv)
    try:
        result = convert(args.value, args.src, args.dst)
    except BelowAbsoluteZeroError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(f"{args.value:g} {args.src} = {result:g} {args.dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
