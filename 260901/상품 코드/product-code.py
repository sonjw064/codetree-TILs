class product:
    def __init__(self, product_name, product_code):
        self.product_name = product_name
        self.product_code = product_code

one = product("codetree", 50)
print(f"product {one.product_code} is {one.product_name}")

product_name, product_code = input().split()
product_code = int(product_code)

two = product(product_name, product_code)
print(f"product {two.product_code} is {two.product_name}")


# Please write your code here.