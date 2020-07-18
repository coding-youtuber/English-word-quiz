import requests
from bs4 import BeautifulSoup

import time
import random

def save_problems():
  """
  スクレイピングして問題を作成、ファイルに保存する
  """
  page_url = "http://www7b.biglobe.ne.jp/~browneye/english/TOEIC400-1.htm"

  r = requests.get(page_url)
  # print(r.encoding)
  # print(r.apparent_encoding)
  r.encoding = r.apparent_encoding

  # return

  soup = BeautifulSoup(r.text, features="html.parser")

  # print(soup)

  td_list = soup.find_all("td")

  # print(td_list)

  td_values = [x.text for x in td_list]

  # print(td_values)

  splited_list = []

  for index in range(0, len(td_values), 4):
    # print(index)
    # print(td_values[index])
    a = td_values[index: index + 4]

    if a[0] == '\u3000':
      continue
    splited_list.append(a)
    # print(td_values[index: index + 4])

  # print(splited_list)

  with open("words.txt", "w") as f:
    for value in splited_list:
      f.write("{},{}\n".format(value[1], value[2]))

def get_problems():
  """
  ファイルから問題と回答のリストを返す

  return 問題と回答のリスト
  """
  with open("words.txt", "r") as f:
    problems = f.readlines()
    # print(problems[0:10])
    problems = [x.strip() for x in problems]

  return problems

def start_english_words_test(problems):
  """
  単語テストを開始する
  英単語と日本語訳を表示
  """
  for index, p in enumerate(problems):
    # print(p)
    x = p.split(",")
    # print(x)

    english = x[0]
    japanese = x[1]
    print("====第{}問目====".format(index + 1))

    print(english)
    time.sleep(1.0)
    print(japanese)
    time.sleep(0.5)
    # break

def main():
  p = get_problems()

  random.shuffle(p)
  
  start_english_words_test(problems=p)


if __name__ == "__main__":
    main()