# Big List of Naughty Files

Script to generate troublesome filenames from the big list of naughty strings:
[blns][blns-1]

[blns-1]: https://github.com/minimaxir/big-list-of-naughty-strings

The output should be useful for testing the file-handling capabilities of
most systems that read files from disk. Digital preservation systems
anticipate a lot of heterogeneous data and so this script is written with
testing those systems in mind.

## Introduction

Big-List-of-Naughty-Files (BLNF) converts the Big List of Naughty
Strings (BLNS) to file names and outputs sample files for each.

* Original by: Max Woolfe converted the list to JSON.

The script tries to convert as many strings from BLNS to file names as
possible.

txt_to_files.py outputs three folders:

```text
    * blnf-output/ <-- contains the two folders below
    * files <-- contains files we were able to write to the file system.
    * converted files <-- contains files we couldn't but simplified the
                          string for, so may still be challenging.
```

You are very likely to have better luck running this script on Linux.
Microsoft control names for example are part of the set.

Is the script dangerous? I don't know. Don't run it as `sudo`.

Files are output as follows:

```text
    ├──output
        ├───files
        └───files-converted
```

And take the form:

    * `<blns-filename>.<unique-string>.blnf`

### Interesting strings

Some interesting strings:

```text
!@#$%^&*()`~
<>?:"{}|_+
Ω≈ç√∫˜µ≤≥÷
```

## Developer install

### pip

Setup a virtual environment `venv` and install the local development
requirements as follows:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements/local.txt
```

### tox

#### Run tests (all)

```bash
python -m tox
```

#### Run tests-only

```bash
python -m tox -e py3
```

#### Run linting-only

```bash
python -m tox -e linting
```

### pre-commit

Pre-commit can be used to provide more feedback before committing code. This
reduces reduces the number of commits you might want to make when working on
code, it's also an alternative to running tox manually.

To set up pre-commit, providing `pip install` has been run above:

* `pre-commit install`

This repository contains a default number of pre-commit hooks, but there may
be others suited to different projects. A list of other pre-commit hooks can be
found [here][pre-commit-1].

[pre-commit-1]: https://pre-commit.com/hooks.html

## Packaging

The `Makefile` contains helper functions for packaging and release.

Makefile functions can be reviewed by calling `make`  from the root of this
repository:

```make
clean                          Clean the package directory
help                           Print this help message.
package-check                  Check the distribution is valid
package-deps                   Upgrade dependencies for packaging
package-source                 Package the source code
package-upload                 Upload package to pypi
package-upload-test            Upload package to test.pypi
tar-source                     Package repository as tar for easy distribution
```

### pyproject.toml

Packaging consumes the metadata in `pyproject.toml` which helps to describe
the project on the official [pypi.org][pypi-2] repository. Have a look at the
documentation and comments there to help you create a suitably descriptive
metadata file.

### Local packaging

To create a python wheel for testing locally, or distributing to colleagues
run:

* `make package-source`

A `tar` and `whl` file will be stored in a `dist/` directory. The `whl` file
can be installed as follows:

* `pip install <your-package>.whl`

### Publishing

Publishing for public use can be achieved with:

* `make package-upload-test` or `make package-upload`

`make-package-upload-test` will upload the package to [test.pypi.org][pypi-1]
which provides a way to look at package metadata and documentation and ensure
that it is correct before uploading to the official [pypi.org][pypi-2]
repository using `make package-upload`.

[pypi-1]: https://test.pypi.org
[pypi-2]: https://pypi.org
