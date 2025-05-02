cart = {}

while True:
    product = input("상품명? ")
    if product == "":
        break
    many = int(input("수량은? "))
    cart[product] = many
    print(f"장바구니에 {product} {many}개가 담겼습니다.\n")

print(f">>> 장바구니 보기: {cart}")

search = input("\n장바구니에서 확인하고자 하는 상품은? ")
if search in cart:
    print(f"{search}는(은) {cart[search]}개 담겨 있습니다.")
else:
    print(f"{search}는(은) 장바구니에 없습니다.")
        
