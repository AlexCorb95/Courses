number_of_cand = int(input())
sizes_of_cand = input()
candel=sizes_of_cand.split()


def birthdayCakeCandles(candles):
    maxim=max(candles)
    return candles.count(maxim)

result = birthdayCakeCandles(candel)
