import argparse
import logging
import sys

from ciprs import VERSION
from ciprs.reader import PDFToTextReader


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("input", help="Path to CIPRS PDF document")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose_count",
        action="count",
        default=0,
        help="increases log verbosity for each occurence.",
    )
    parser.add_argument(
        "--source", help="Include full source in JSON output", action="store_true"
    )
    parser.add_argument("--version", action="version", version="%(prog)s " + VERSION)
    args = parser.parse_args()
    formatter = logging.Formatter("%(levelname)s %(asctime)s %(name)s %(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger = logging.getLogger("ciprs")
    logger.addHandler(handler)
    logger.setLevel(max(3 - args.verbose_count, 0) * 10)

    logger.info("Running ciprs-reader on %s", args.input)
    reader = PDFToTextReader(args.input)
    reader.parse(source=args.source)
    print(reader.json())
