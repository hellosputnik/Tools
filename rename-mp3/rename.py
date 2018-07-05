#!/usr/bin/env python3

import fire
import mutagen.mp3
import os
import shutil
import sys

class Rename:
    def rename(self, file_name):
        try:
            # Get the base directory of the MP3 file.
            abspath   = os.path.abspath(file_name)
            directory = os.path.dirname(abspath)

            # Get the title of the MP3 file.
            metadata = mutagen.mp3.EasyMP3(file_name)
            title    = metadata.get("title")[0]

            # Rename the MP3 file.
            shutil.move(file_name, "{}/{}.mp3".format(directory, title))

            # Log the operation.
            print("\{}.mp3 => {}/{}.mp3".format(file_name, directory, title))
        except Exception as e:
            print("There was an error with {}: {}\n".format(file_name, e))

    def renames(self, directory):
        # Rename all the MP3 files in the given directory (non-recursive).
        for base_path, directories, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp3"):
                    self.rename("{}/{}".format(base_path, file))


def main():
    fire.Fire(Rename)


if __name__ == '__main__':
    main()

