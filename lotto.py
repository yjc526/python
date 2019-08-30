import random
import requests

lotto = sorted(random.sample(range(1,46),6))

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873"
res = requests.get(url)
data = res.json()

winner = []

for i in range(1,7):
    winner.append(data[f'drwtNo{i}'])

cnt = len(set(lotto) & set(winner))

