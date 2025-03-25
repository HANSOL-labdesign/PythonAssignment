def exchange(amount):
    coin_500 = amount // 500
    cal_500 = amount % 500
    
    coin_100 = cal_500 // 100
    cal_100 = cal_500 % 100

    coin_50 = cal_100 // 50
    cal_50 = cal_100 % 50

    coin_10 = cal_50 // 10
    
    return coin_500, coin_100, coin_50, coin_10

def get_integer(prompt):
    res = int(input(prompt))
    return res

amount = get_integer("동전으로 교환하고자 하는 금액은? ")

coin_500, coin_100, coin_50, coin_10 = exchange(amount)

print(f"500원 동전의 개수: {coin_500}")
print(f"100원 동전의 개수: {coin_100}")
print(f"50원 동전의 개수: {coin_50}")
print(f"10원 동전의 개수: {coin_10}")