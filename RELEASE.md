# Big List of Naughty Files (BLNF)

Files with filenames generated from the big list of naughty strings
'[blns][blns-1]' using a custom Python script [blnf][blns-2]. BLNF is by
Independent Digital Preservation Researcher, Ross Spencer.

[blns-1]: https://github.com/minimaxir/big-list-of-naughty-strings
[blns-2]: https://github.com/ross-spencer/big-list-of-naughty-files

The output should be useful for testing the file-handling capabilities of
most systems that read files from disk. Digital preservation systems
anticipate a lot of heterogeneous data and so this script is written with
testing those systems in mind.

## BLNF

Big-List-of-Naughty-Files (BLNF) converts the Big List of Naughty
Strings (BLNS) by Max Woolf to file names and outputs sample files for each.

Files are output as follows:

```text
    ├──blnf-output
        ├───files
        └───files-converted
```

And take the form:

    * `<blns-filename>.<unique-string>.blnf`

At the time of writing the script outputs: `2 directories, 511 files` on
`Ubuntu 22.04.4 LTS` running `Python 3.12.3`.

### Checksums

Two manifests are included in the `7z` file for validating the contents on
extract.

In the current release:

* md5 = `e049fd364abc35f24fd66f056d30f95c`
* sha256 = `37b1ccdafd72a526d4f65b8f072c61c29bb71d77708873daf71348d96a709443`

#### Duplicates

Systems will need to be aware that all the files are duplicates of one anohter
with the exception of their filenames. Thie should be accounted for in testing.

### Filenames

Filenames that are generated are guaranteed to be unique and a partial UUID is
appended to each filename.

### Datetimes

All files have the modified timestamp 14 July 2004.

### Interesting strings

Some interesting and innocuous looking strings I have found that some systems
struggle with:

```text
!@#$%^&*()`~
<>?:"{}|_+
Ω≈ç√∫˜µ≤≥÷
```

### 7z

The package format is 7z (7-zip) and is named zip for GitHub releases. Use
7zip for the most compatible extract, other decompress tools may not
perform equally.

### Caution

Use with caution. Use only on non-production servers that you can easily
restore.
