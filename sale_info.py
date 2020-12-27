# 销售信息 实体
class SaleInfo:
    buy = ''
    province = ''
    good = ''
    color = ''
    price = ''
    discountPrice = ''

    def __init__(self, buy, province, good, color, price, discountPrice):
        self.buy = buy
        self.province = province
        self.good = good
        self.color = color
        self.price = price
        self.discountPrice = discountPrice