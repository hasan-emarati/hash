# created from SHe
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from Tools.Hash import Hash
    from Tools.choice import choice
    from Tools.main import main

except ImportError as err:
    main("Failed import some modules", err)
    sys.exit(1)


if __name__ == "__main__":
    choice()
    sys.exit(1)

