# all letters before the initial vowel are placed at the end of the word, then "ay" is added.
# pig->> igpay
# trash->> ashtr
# vowel aeiou eat->eatway

# sentence= "Today is my birthday"
# sentence="I am a Stevens Software Engineer"
# sentence="Is Charles Xavier an Xman or is he Captain Picard"
# sentence="Lets meet at the ADS Lab"
# sentence="Software engineers shall ensure that their products meet the highest professional standards possible.
# They shall maintain integrity and independence in their professional judgment"
# python piglatin.py

from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', method=['POST'])
def getvalue():
    eng = request.form['eng']
    return render_template("pass.html", eng=eng)


if __name__ == '__main__':
    app.run(debug=True)


class Translate:

    sentence = input("Enter your value: ")
    sentence = sentence.lower()
    word = sentence.split()
    length = len(word)

    i = 0
    complete_trans = ""
    while i < length:
        alphabet = word[i][0]
        trans = ""
        v = ""

        if 'a' in word[i]:
            v = 1
        elif 'e' in word[i]:
            v = 1
        elif 'i' in word[i]:
            v = 1
        elif 'o' in word[i]:
            v = 1
        elif 'u' in word[i]:
            v = 1
        else:
            v = 0

        # words without vowel
        if v == 0:
            trans = word[i]

        # words that has vowel in
        else:

            # starts with vowel
            if alphabet in "aeiouAEIOU":
                trans=word[i]+"way"

            # begins with vowel but has vowel in
            elif alphabet not in "aeiouAEIOU":
                aa = word[i].find('a')
                ee = word[i].find('e')
                ii = word[i].find('i')
                oo = word[i].find('o')
                uu = word[i].find('u')
                index = [aa, ee, ii, oo, uu]
                new_list = list(set(index))
                new_list.sort()
                n = new_list[1]
                trans = word[i][n:]+word[i][0:n]+"ay"

        print(i, ": ", trans)
        i = i+1
        complete_trans += trans+" "

    print("English:", sentence)
    print("PigLatin:", complete_trans.capitalize())

