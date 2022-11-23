from googletrans import Translator
import os
import httpcore
from tabulate import tabulate
import openfile
# import write_to_file
# from mypcg import select, test
import arabic_reshaper
from bidi.algorithm import get_display


class Cheking:

    @staticmethod
    def checking(dic, text, null=0, online=0):

        if dic is not None and text in dic.keys():
            alpha_en = 'abcdefghijklmnopqrstuvwxyz'
            alpha_farsi = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
            os.system('cls')

            c = 0
            alph_text = ''
            for i in alpha_en:
                if i in dic[text]:
                    c += 1
            if c >= 1:
                alph_text = 'Английский'
                c = 0
            else:
                c = 0
                for i in alpha_farsi:
                    if i in dic[text]:
                        c += 1
                if c >= 1:
                    alph_text = 'Персидский'
                    c = 0
                else:
                    c = 0
                    alph_text = "Русский"

            # -----------чтобы можно было фарси писать и ситать в cmd
            #########################################################
            #########################################################
            #########################################################


            reshaped = arabic_reshaper.reshape(dic[text])
            bidi_tex1 = get_display(reshaped)

            #########################################################
            #########################################################
            #########################################################
            #########################################################

            lst_translate = [[f'перевод на ---{alph_text}---   '],
                             ['\033[31m' + '\033[1m' + dic[text].center(25, " ")]]
            print(
                colors.style.RESET_ALL + colors.fg.CYAN + tabulate(lst_translate, tablefmt="grid", )
                + colors.style.RESET_ALL + '\n')

            st_translate = []
            for i, j in dic.items():
                if j == dic[text] and i != text:
                    for e in alpha_en:
                        if e in i:
                            c += 1
                    if c >= 1:
                        alph_text = 'Английский'
                        c = 0
                    else:
                        c = 0
                        for e in alpha_farsi:
                            if e in i:
                                c += 1
                        if c >= 1:
                            alph_text = 'Персидский'
                            c = 0
                        else:
                            c = 0
                            alph_text = "Русский"
                    reshaped = arabic_reshaper.reshape(i)
                    bidi_tex2 = get_display(reshaped)
                    st_translate.append([f'перевод  на -{alph_text}-' + i.center(25, " ")])
            print(colors.style.RESET_ALL + colors.fg.CYAN + tabulate(st_translate, tablefmt="grid", )
                  + colors.style.RESET_ALL + '\n')

            ########################################################
            #########################################################
            ########################################################
            #########################################################

        elif dic is not None and text in dic.values():
            alpha_en = 'abcdefghijklmnopqrstuvwxyz'
            alpha_farsi = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
            c = 0
            os.system('cls')
            for i, j in dic.items():
                if j == text:
                    for e in alpha_en:
                        if e in i:
                            c += 1
                    if c >= 1:
                        alph_text = 'Английский'
                        c = 0
                    else:
                        c = 0
                        for e in alpha_farsi:
                            if e in i:
                                c += 1
                        if c >= 1:
                            alph_text = 'Персидский'
                            c = 0
                        else:
                            c = 0
                            alph_text = "Русский"
                    reshaped = arabic_reshaper.reshape(i)
                    bidi_tex3 = get_display(reshaped)
                    st_translate = [[f'перевод на ---{alph_text}---'],
                                    ['\033[31m' + '\033[1m' + i.center(25, " ")]]
                    print(
                        colors.style.RESET_ALL + colors.fg.CYAN + tabulate(st_translate, tablefmt="grid", )
                        + colors.style.RESET_ALL + '\n')

                    ########################################################
                    #########################################################
                    ########################################################
                    #########################################################

        elif online == 1 or null == 1 or dic is not None \
                and text not in dic.keys() and text not in dic.values():

            if online == 1:
                write_to_file.Write_To_File.read_suggest_dic_online(text)

            else:
                write_to_file.Write_To_File.read_suggest_dic_offline(text)

        elif dic is None:

            Cheking.checking(dic, text, 1)

            #########################################################
            #########################################################
            ########################################################
            #########################################################

    @staticmethod
    def choose(arg=""):

        lst_choose = ['1', '3', '2', '4', '0']
        print("введите еще раз правильное слово или \nвыберите [1][2][3][4][0] ->:  -> ", end="")
        right_word = input().lower().strip()
        while not right_word.isalpha() and right_word not in lst_choose:
            print("введите еще раз правильное слово:  -> ", end="")
            right_word = input().lower().strip()
        if right_word in lst_choose:
            select.select_action(right_word)

        text = right_word
        read = openfile.OpenFile()
        dic = read.opening_json('dictionary.json')

        Cheking.checking(dic, text)
