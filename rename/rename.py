#!/usr/bin/env python3

import fire
import logging
import mutagen.mp3
import os
import re
import shutil


log = logging.getLogger(__name__)


class Rename:
    def search_and_replace(self, old_name, search, replace):
        return re.sub(search, replace, old_name)

    def delete_parentheses(self, name):
        return self.search_and_replace(name, "\(.*\)", '')

    def delete_whitespace(self, name):
        return self.search_and_replace(name, "\s{2,}", ' ')

    def rename_rom(self, file_name):
        # Get the base directory of the ROM file.
        abspath   = os.path.abspath(file_name)
        dirname   = os.path.dirname(abspath)

        # Delete all unnecessary characters from the name.
        name = self.delete_parentheses(file_name)
        name = self.search_and_replace(name, '-', replace='：')
        name = self.search_and_replace(name, '\s+：', replace='：')
        name = self.search_and_replace(name, '_', replace=' ')
        name = self.delete_whitespace(name)

        # Rename the ROM file.
        shutil.move(file_name, "{}/{}".format(dirname, name))

        return name

    def rename_mp3(self, file_name):
        # Get the base directory of the MP3 file.
        abspath = os.path.abspath(file_name)
        dirname = os.path.dirname(abspath)

        # Get the title of the MP3 file.
        metadata = mutagen.mp3.EasyMP3(file_name)
        title    = metadata.get("title")[0]

        # Rename the MP3 file.
        shutil.move(file_name, "{}/{}.mp3".format(dirname, title))

        return title


def main():
    fire.Fire(Rename)


if __name__ == '__main__':
    main()

