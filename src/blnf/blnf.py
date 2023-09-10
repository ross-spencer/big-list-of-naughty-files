"""Big-List-of-Naughty-Files (BLNF) converts the Big List of Naughty
Strings (BLNS) to file names and outputs sample files for each.

    * Original by: Max Woolfe converted the list to JSON.

The script tries to convert as many strings from BLNS to file names as
possible.

txt_to_files.py outputs three folders:

    * blnf-output/ <-- contains the two folders below
    * files <-- contains files we were able to write to the file system.
    * converted files <-- contains files we couldn't but simplified the
                          string for, so may still be challenging.

You are very likely to have better luck running this script on Linux.
Microsoft control names for example are part of the set.

Is the script dangerous? I don't know. Don't run it as `sudo`.

Files are output as follows:

    ├──output
        ├───files
        └───files-converted

And take the form:

    * `<blns-filename>.<unique-string>.blnf`

"""

import logging
import os
import shutil
import time
import uuid
from pathlib import Path
from typing import Final

from slugify import slugify

# Set up logging.
logging.basicConfig(
    format="%(asctime)-15s %(levelname)s :: %(filename)s:%(lineno)s:%(funcName)s() :: %(message)s",  # noqa: E501
    datefmt="%Y-%m-%d %H:%M:%S",
    level="INFO",
    handlers=[
        logging.StreamHandler(),
    ],
)

# Format logs using UTC time.
logging.Formatter.converter = time.gmtime


logger = logging.getLogger(__name__)


BLNS_LOC: Final[str] = "blns.txt"
OUTPUT: Final[str] = "blnf-output"
FILES: Final[str] = "files"
CONVERTED: Final[str] = "files-converted"


def process_strings_to_list() -> list:
    """Converts our strings to a list."""
    strings = []
    script_dir = os.path.dirname(os.path.realpath(__file__))
    strings_loc = Path(script_dir) / Path(BLNS_LOC)
    with open(strings_loc, "r", encoding="utf8") as blns:
        idx = 0
        for idx, line in enumerate(blns):
            try:
                # above line leaves trailing newline characters; strip them out
                line = line.strip("\n")
                # remove empty-lines and comments
                if line.startswith("#"):
                    continue
                if not line:
                    continue
                strings.append(line)
                continue
            except UnicodeDecodeError as err:
                logger.info("cannot convert to list: %s", err)
                continue
        logger.info("files output to list: %s", idx)
    return strings


def _create_dirs(path1: Path, path2: Path) -> None:
    """Create the directories we want to write to. If the directories
    exist, delete them, call the function again.
    """
    try:
        for path in (path1, path2):
            path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        shutil.rmtree(str(path1))
        shutil.rmtree(str(path2))
        _create_dirs(path1, path2)


def bind_to_files(strings: list) -> None:
    """Writes our strings as filenames."""
    err_no = 0
    path1 = Path(OUTPUT) / FILES
    path2 = Path(OUTPUT) / CONVERTED
    _create_dirs(path1, path2)
    logger.info("expected no. files (optimistic): '%s'", len(strings))
    # Ensure the files have a consistent extension and some content.
    ext: Final[str] = "blnf"
    content = "Created from the Big List of Naughty Strings™"
    for file in strings:
        try:
            # Ensure that the full filename is unique.
            unique = str(uuid.uuid4())[:8]
            with open(
                os.path.join(str(path1), f"{file}.{unique}.{ext}"),
                "w",
                encoding="UTF-8",
            ) as naughty_file:
                # Write something to the file to provide a unique
                # digital signature / checksum.
                naughty_file.write(content)
        except (FileNotFoundError, OSError) as err:
            err_no += 1
            converted_file = slugify(
                file,
                allow_unicode=True,
                lowercase=False,
                save_order=True,
                separator="_",
            )
            logger.info(
                "cannot write file: '%s' converting to '%s' %s",
                err,
                converted_file,
                err_no,
            )
            if not converted_file:
                continue
            try:
                # Ensure that the full filename is unique.
                unique = str(uuid.uuid4())[:8]
                with open(
                    os.path.join(str(path2), f"{converted_file}.{unique}.{ext}"),
                    "w",
                    encoding="UTF-8",
                ) as converted:
                    converted.write(content)
            except (IsADirectoryError, OSError) as secondary_err:
                logging.info(
                    "finally, cannot write: '%s' '%s'", converted_file, secondary_err
                )
            continue


def main() -> None:
    """Primary entry point for this script."""
    strings = process_strings_to_list()
    bind_to_files(strings)


if __name__ == "__main__":
    main()
