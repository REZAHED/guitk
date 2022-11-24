import os

import httpcore
from googletrans import Translator
from tabulate import tabulate




import openfile
import json


class Write_To_File:
    os.system('cls')

    # def __init__(self, a="" ,b=""):
    #     self.a=a
    #     self.b=b

    def dic_to_file(self, word, translate):
        self.a = word
        self.b = translate

        read = openfile.OpenFile()
        dic_en_rus = read.opening_json('dictionary.json')
        if dic_en_rus is not None:
            dic_en_rus.update({word: translate})
        else:
            dic_en_rus = {word: translate}
        with open('dictionary.json', 'r+', encoding='utf-8-sig') as file:
            json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
            os.system('cls')
        return  f'Слово {word.upper()} и его значение\n {translate.upper()} успешно сохранены.'

    #########################################################
    #########################################################
    #########################################################
    #########################################################

    def updat(self, dic):

        with open('dictionary.json', 'w+', encoding='utf-8-sig') as file:
            json.dump(dic, file, indent=2, ensure_ascii=False)
            os.system('cls')

    #########################################################
    #########################################################
    #########################################################
    #########################################################

    @staticmethod
    def online_translate(text):
        lst_record = []
        lst_lang = ['fa', 'en', 'ru']
        translator = Translator()

        print('на какой язык хотите перевести\nперсидский[fa],русский[ru],английский[en] ->:', end="")
        dest_lang = input("")
        while dest_lang not in lst_lang:
            print('введите персидский[fa],русский[ru],английский[en] ->:', end="")
            dest_lang = input("")
        try:

            st = translator.translate(text, src='auto', dest=dest_lang)

        except:
            httpcore._exceptions.ConnectError()
            print("нет интернета")
        else:

            lst_record = [[Write_To_File().dic_to_file(text, st.text)]]
        return  tabulate(lst_record, tablefmt="grid", ) +  '\n'

    #########################################################
    #########################################################
    #########################################################
    #########################################################

    # @staticmethod
    # def read_suggest_dic_online(text):
    #
    #     lines = openfile.OpenFile.open_dictionary(text)
    #
    #
    #         # write_to = Write_To_File()
    #
    #
    #     transalte = Write_To_File.online_translate(text)
    #
    #
    #
    #
    #         print("\nэтого слова нет в словаре русского языка\nи не записано в вашем словаре\n")
    #
    #         suggest_lst = test.suggest(text, lines)
    #
    #         del lines
    #         if suggest_lst:
    #             print(colors.fg.RED + 'может вы имели ввиду -> :', end="")
    #             for i in range(len(suggest_lst)):
    #                 print(colors.fg.YELLOW + f' {i + 5}.{suggest_lst[i]}', end='' + colors.style.RESET_ALL)
    #                 if i == 4:
    #                     print('\n', end="")
    #                 if i == 9:
    #                     print("\n")
    #                     break
    #             print("\nвы правильно написали? выберите [+]ДА , [-]НЕТ \nили введите номер из предложений -> : ",
    #                   end="")
    #         else:
    #             print("\nвы правильно написали? выберите [+]ДА , [-]НЕТ  -> : ", end="")
    #         check = input().lower().strip()
    #         check_lst = ["+", "-"]
    #         lst_choose = ['1', '3', '2', '4', '0']
    #         lst_choose_text = []
    #         for i in range(len(suggest_lst)):
    #             if i == 10:
    #                 break
    #             else:
    #                 lst_choose_text.append(str(i + 5))
    #         # else:
    #         while check not in check_lst and check not in lst_choose and check not in lst_choose_text:
    #             check = input("введите ' + ' или ' - '   :-> ").lower().strip()
    #         if check in lst_choose:
    #             os.system('cls')
    #             select.select_action(check)
    #
    #         if check in lst_choose_text:
    #             text = suggest_lst[int(check) - 5]
    #             os.system('cls')
    #             print(colors.fg.YELLOW + f' вы выбрали слово : {text}' + colors.style.RESET_ALL)
    #             transalte = Write_To_File.online_translate(text)
    #             print(transalte)
    #             select.select_action("4")
    #
    #         del suggest_lst
    #         del lst_choose_text
    #
    #         if check == '+':
    #             os.system('cls')
    #             transalte = Write_To_File.online_translate(text)
    #             print(transalte)
    #
    #         elif check == "-":
    #             cheking.Cheking.choose()

    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################

    # @staticmethod
    # def read_suggest_dic_offline(text):
    #
    #     lines = openfile.OpenFile.open_dictionary(text)
    #
    #     if text.lower() in lines:
    #
    #         lst_choose = ['1', '3', '2', '4', '0']
    #         write_to = Write_To_File()
    #
    #         print('\033[32m' + '\033[1m' + "Данное слово не записано в словаре!! ")
    #         print("\nВведите его значение \n для записи в словарь: -> ", end="")
    #         text_translate = input().lower().strip()
    #         while not text_translate.replace(" ", '').isalpha() and text_translate not in lst_choose:
    #             print("Введите правильное значение или :\n выберите [1][2][3][4][0] -> ", end="")
    #             text_translate = input().lower().strip()
    #             os.system('cls')
    #         if text_translate in lst_choose:
    #             os.system('cls')
    #             select.select_action(text_translate)
    #         else:
    #             lst_record = [[write_to.dic_to_file(text, text_translate)]]
    #             print(colors.style.RESET_ALL + colors.fg.RED
    #                   + tabulate(lst_record, tablefmt="grid", ) + colors.style.RESET_ALL + '\n')
    #             select.select_action("1")
    #     else:
    #
    #         write_to = Write_To_File()
    #         print("\nэтого слова нет в словаре русского языка\nи не записано в вашем словаре\n")
    #
    #         suggest_lst = test.suggest(text, lines)
    #
    #         del lines
    #         # sugg_text = ""
    #         if suggest_lst:
    #             print(colors.fg.RED + 'может вы имели ввиду -> :', end="")
    #             for i in range(len(suggest_lst)):
    #                 print(colors.fg.YELLOW + f' {i + 5}.{suggest_lst[i]}', end='' + colors.style.RESET_ALL)
    #                 if i == 4:
    #                     print('\n', end="")
    #                 if i == 11:
    #                     print("\n")
    #                     break
    #             print("\nвы правильно написали? выберите [+]ДА , [-]НЕТ \nили введите номер из предложений -> : ",
    #                   end="")
    #         else:
    #             print("\nвы правильно написали? выберите [+]ДА , [-]НЕТ  -> : ", end="")
    #         check = input().lower().strip()
    #
    #         check_lst = ["+", "-"]
    #         lst_choose = ['1', '3', '2', '4', '0']
    #         lst_choose_text = []
    #
    #         for i in range(len(suggest_lst)):
    #             if i == 12:
    #                 break
    #             else:
    #                 lst_choose_text.append(str(i + 5))
    #         # else:
    #         while check not in check_lst and check not in lst_choose and check not in lst_choose_text:
    #             check = input("введите ' + ' или ' - '   :-> ").lower().strip()
    #         if check in lst_choose:
    #             os.system('cls')
    #             select.select_action(check)
    #
    #         if check in lst_choose_text:
    #             text = suggest_lst[int(check) - 5]
    #             print(colors.fg.YELLOW + f' вы выбрали слово : {text}' + colors.style.RESET_ALL)
    #
    #             print("\nВведите его значение \nили выберите [1][2][3][4][0] из меню -> ", end="")
    #             text_translate = input().lower().strip()
    #
    #             while not text_translate.replace(" ", '').isalpha() and text_translate not in lst_choose:
    #                 print("Введите правильное значение: -> ", end="")
    #                 text_translate = input().lower().strip()
    #                 os.system('cls')
    #             if text_translate in lst_choose:
    #                 os.system('cls')
    #                 select.select_action(text_translate)
    #             else:
    #
    #                 lst_record = [[Write_To_File().dic_to_file(text, text_translate)]]
    #                 print(colors.style.RESET_ALL + colors.fg.RED
    #                       + tabulate(lst_record, tablefmt="grid", ) + colors.style.RESET_ALL + '\n')
    #         del suggest_lst
    #         del lst_choose_text
    #
    #         if check == '+':
    #             print("\nВведите его значение \n для записи в словарь: -> ", end="")
    #             text_translate = input().lower().strip()
    #
    #             while not text_translate.replace(" ", '').isalpha() and text_translate not in lst_choose:
    #                 print("Введите правильное значение: -> ", end="")
    #                 text_translate = input().lower().strip()
    #                 os.system('cls')
    #             if text_translate in lst_choose:
    #                 os.system('cls')
    #                 select.select_action(text_translate)
    #             else:
    #                 lst_record = [[Write_To_File().dic_to_file(text, text_translate)]]
    #                 print(colors.style.RESET_ALL + colors.fg.RED
    #                       + tabulate(lst_record, tablefmt="grid", ) + colors.style.RESET_ALL + '\n')
    #
    #         elif check == "-":
    #             cheking.Cheking.choose()
