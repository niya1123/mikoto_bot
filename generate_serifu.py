import MeCab
import random


def wakati():
    """
    Mecabを用いた形態素解析。
    """

    # text = """
    # ごめぇーんまったぁ〜？まったって言ってんでしょ！無視すんなやゴッラァー
    # どこ触ってんだよコラァ！！！
    # あんた本当に大学生？
    # ごめんね気づいてあげれなくて。でもさもう一度頑張ってみよう？
    # もう一度頑張ってみよ。こんなところでくよくよしてないで自分で自分に嘘つかないでもう一度…
    # アンタにやって欲しい事があるの。ううんアンタにしかできない事があるの！
    # """
    with open('serifu.txt', 'r') as f:
        text = f.read()
    print(text)
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    for r in result:
        if r == "\u3000":
            result.remove(r)
    print(result)
    return result


def create_serifu(wordlist):
    """
     ６連マルコフ連鎖。

     parametaers
     -----------
     wordlist: list
        wakatiで形態素解析された単語のリスト。
    """
    markov = {}
    w1 = ""
    w2 = ""
    w3 = ""
    w4 = ""
    w5 = ""
    w6 = ""
    endword = ["。", "？", "！", "…"]
    # continuedword = ["ー","〜","、"]

    for word in wordlist:
        if w1 and w2 and w3 and w4 and w5 and w6:
            if (w1, w2, w3, w4, w5, w6) not in markov:
                markov[(w1, w2, w3, w4, w5, w6)] = []
            markov[(w1, w2, w3, w4, w5, w6)].append(word)
        w1, w2, w3, w4, w5, w6 = w2, w3, w4, w5, w6, word

    count = 0
    sentence = ""
    word_list = list(markov.keys())
    w1, w2, w3, w4, w5, w6 = random.choice(word_list)

    while count < len(wordlist):
        tmp = random.choice(markov[w1, w2, w3, w4, w5, w6])
        if tmp in endword:
            sentence += tmp
            break
        sentence += tmp
        w1, w2, w3, w4, w5, w6 = w2, w3, w4, w5, w6, tmp
        count += 1
        if count > 1000:
            break
    return sentence


def main():
    """
    main関数。wakatiと、create_serifuのオブジェクトの生成をしている。
    """
    wordlist = wakati()
    serifu = create_serifu(wordlist)
    print(serifu)

    return serifu
