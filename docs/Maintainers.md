<!--
===-----------------------------------------------------------------------------------===
Copyright (c) 2021 Calinescu Mihai

For copying notice, see https://github.com/CMihai99/python-projects/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/python-projects/tree/main/LICENSES.
===-----------------------------------------------------------------------------------===
-->

# List of Maintainers

Please try to follow the guidelines and entry descriptions below. This will make
things easier on the maintainers. Not all guidelines apply to every patch.

When adding to this list, please keep entries in alphabetical order.

Do not add any entries after EVERYTHING ELSE. That will be at the end of this file.

## Tips for patch submitters

1.  Always test your changes, however small, on at least 2 people, preferably more.

2.  Make sure your changes compile correctly in multiple configurations.
    In particular, check that changes are both responsive and functional.

3.  When you are happy with a change, make it generally available for testing and await feedback.

4.  Make a patch available to the relevant maintainer in the list. Use `diff -u`
    to make the patch easy to merge. Be prepared to get your changes sent back with
    seemingly silly requests about formatting and naming. These aren't as silly
    as they seem. One job the maintainers (and especially Mihai) do is keep things
    looking the same. Sometimes this means that the clever hack in your code to get
    around a problem needs to become a feature ready for next time.

    Try to include any credit lines you want added with the patch.

    Document known bugs. If it doesn't work for everything or
    it does something very odd once a month, document it.

    Remember that submissions must be made under the terms of the certificate
    of contribution and should include a `Signed-off-by:` line. The current version
    of the "Developer's Certificate of Origin" (DCO) is listed in [SubmittingPatches.md](https://github.com/CMihai99/python-projects/blob/main/docs/how-to/maintaining/SubmittingPatches.md).

5.  Always add 2 trailing spaces at the end of each attribute (e.g. S: Maintained  )

## Section entry descriptions

-   R: Reviewer: Your Name <yourmail@yourhost.com>

-   M: Mail: Your Name <yourmail@yourhost.com>

-   S: Status: One of the following:

    -   Supported: Someone is paid to look after this.

    -   Maintained: Someone looks after it.

    -   Odd Fixes: It has a maintainer but they don't have time to do much
        other than throw the odd patch in.

    -   Orphan: No current maintainer (but maybe you could take the role).

    -   Obsolete: Old code. Something tagged obsolete generally means
        it has been replaced by a newer version.

-   F: Files: Files and directories wildcard patterns.
    A trailing slash includes all files and subdirectory files.
    One pattern per line. Multiple F: lines are acceptable.

-   X: Excluded: Excluded files and directories that are not maintained,
    same rules as F. Files exclusions are tested before file matches.
    Can be useful for excluding a specific subdirectory.

## Maintainers list

EVERYTHING ELSE  
R: Mihai Calinescu <mihaimihaia431@gmail.com>  
M: Mihai Calinescu <mihaimihaia431@gmail.com>  
S: Maintained  
F: *  
