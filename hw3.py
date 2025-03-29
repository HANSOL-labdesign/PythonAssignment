def get_fixed_price(dRate, dPrice):
    oPrice = dPrice * 100 / (100 - dRate)
    return int(oPrice)

dRate = int(input("할인율은? "))

dPrice_a = int(input("A 상품의 할인된 가격은? "))

dPrice_b = int(input("B 상품의 할인된 가격은? "))

oPrice_a = get_fixed_price(dRate, dPrice_a)
oPrice_b = get_fixed_price(dRate, dPrice_b)

print(f"A 상품의 정가는 {oPrice_a}원")
print(f"B 상품의 정가는 {oPrice_b}원")
