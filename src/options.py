from typing import List
from os import path

ERROR_ARGUMENT = 1
SUCCESS = 0


class Options:

    def __init__(self, argv: List[str]) -> None:
        self.argv = argv
        self.argc = len(argv)
        self.options = ".md"

        self.path: str

    # COMMANDES
    def process_argument(self) -> bool:
        """
        Process command line argument and return 0
        if success a positive value else.
        """
        for arg in self.argv[1:]:
            if self.is_option(arg):
                self.options = "." + arg[1:]
            elif self.is_file(arg) or self.is_dir(arg):
                self.path = arg
            else:
                self.__error_argument(arg)
                return ERROR_ARGUMENT
        return SUCCESS

    # REQUETES
    def get_path(self) -> str:
        """Return the path of the file or dir."""
        return self.path

    def get_option(self) -> str:
        """Return the current file format for the documentation."""
        return self.options
    
    def get_argc(self) -> int:
        """Return the number of argument on the command line."""
        return self.argc

    def is_in_argv(self, s: str) -> bool:
        """Return if s is in command line arguments."""
        for arg in self.argv:
            if arg == s:
                return True
        return False

    def is_option(self, s: str) -> bool:
        """Return if s is a valid option."""
        opts = ["-html", "-pdf", "-md"]
        return s in opts

    def is_file(self, s: str) -> bool:
        """Return if s is a valid file."""
        return path.isfile(s)

    def is_dir(self, s: str) -> bool:
        """Return if s is a valid dir."""
        return path.isdir(s)

    # OUTPUT
    @staticmethod
    def unexpected_argument() -> None:
        """Print unexpected information."""
        print("pad: At least one path is expected.")
        print("Try 'pad --help' for more information.")

    @staticmethod
    def help__() -> None:
        """Print help option."""
        opt_desc = {
            "-html": "Convert output to a html file",
            "-pdf": "Convert output to a pdf file.",
            "-md": "Convert output to a markdown file."
        }

        print("Usage: pad [OPTION]... PATH\n")
        print("Make a documentation by default a markdown"
              " of a python file or directory.\n")
        print("Option:")
        for name, desc in opt_desc.items():
            print("\t" + name + "\t" + desc)

    @staticmethod
    def __error_argument(s: str) -> None:
        print(f"pad: Argument error '{s}'")