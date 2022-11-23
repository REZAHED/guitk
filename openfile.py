import json
import os


class OpenFile:

    @staticmethod
    def opening_read(self):
        with open(self, 'r', encoding='utf-8-sig') as file:
            return file.read()


    @staticmethod
    def opening_json(self):
        if os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') !=0:

        # if os.path.getsize('dictionary.json') !=0:
            with open(self, 'r', encoding='utf-8-sig') as file:
                return json.load(file)
        elif not os.path.exists('dictionary.json'):
            file = open('dictionary.json', 'a+', encoding='utf-8-sig')
            file.close()
            return None
        elif os.path.exists('dictionary.json') and os.path.getsize('dictionary.json') ==0:
            return None


    @staticmethod
    def open_dictionary(text) -> list:
        with open('slov_russ_dic.txt', 'r', encoding='utf-8') as file:
            if len(text) == 1:
                lines = [line.rstrip() for line in file.readlines() if len(line.rstrip()) == 1]

            elif len(text) == 2:
                lines = [line.rstrip() for line in file.readlines() if len(line.rstrip()) == 2]
            elif len(text) >= 3:
                lines = [line.rstrip() for line in file.readlines()
                         if len(line.rstrip()) == len(text) + 1
                         or len(line.rstrip()) == len(text)]
        return lines