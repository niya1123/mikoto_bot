import MeCab
import random


def wakati():

    text = """
    ごめぇーんまったぁ〜？まったって言ってんでしょ！無視すんなやゴッラァー
    どこ触ってんだよコラァ！！！
    あんた本当に大学生？
    ごめんね気づいてあげれなくて。でもさもう一度頑張ってみよう？
    もう一度頑張ってみよ。こんなところでくよくよしてないで自分で自分に嘘つかないでもう一度…
    アンタにやって欲しい事があるの。ううんアンタにしかできない事があるの！
    """

    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result


def create_serifu(wordlist):
    markov = {}
    w1 = ""
    w2 = ""
    w3 = ""
    endword = ["。", "？", "！", "…"]

    for word in wordlist:
        if w1 and w2 and w3:
            if (w1, w2, w3) not in markov:
                markov[(w1, w2, w3)] = []
            markov[(w1, w2, w3)].append(word)
        w1, w2, w3 = w2, w3, word

    count = 0
    sentence = ""
    w1, w2, w3 = random.choice(list(markov.keys()))

    while count < len(wordlist):
        tmp = random.choice(markov[w1, w2, w3])
        if tmp in endword:
            sentence += tmp
            break
        sentence += tmp
        w1, w2, w3 = w2, w3, tmp
        count += 1
        if count > 20:
            break
    return sentence


def main():
    wordlist = wakati()
    serifu = create_serifu(wordlist)

    return serifu
