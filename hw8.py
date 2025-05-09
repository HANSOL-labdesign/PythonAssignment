def buy(shopping_bag):
    print("[구입}")
    product = input("상품명? ")
    if product == "":
        return False
    nums = int(input("수량은? "))
    if product in shopping_bag:
        shpping_bag[product] += nums
    else:
        shopping_bag[product] = nums
    print(f"장바구니에 {product} {nums}개가 담겼습니다.")
    print()
    return True

def show(shopping_bag):
    print(f">>> 장바구니 보기 : {shopping_bag}")
    print()

def find(shopping_bag):
    print("[검색]")
    search = input("장바구니에서 확인하고자 하는 상품은? ")
    if search in shopping_bag:
        print(f"{search}는(은) {shopping_bag[search]}개 담겨 있습니다.")
    else:
        print(f"{search}는(은) 장바구니에 없습니다.")
    
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
