import logging
import sys

from ._cli import ApiHunterCli


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )
    ApiHunterCli(sys.argv[1:]).run()


if __name__ == "__main__":
    main()
