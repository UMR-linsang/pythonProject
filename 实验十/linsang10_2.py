# 定义Product类
class Product():
    # 定义成员属性（实例属性）
    def __init__(self, id, name=";", num=0, price=0):
        self.id = id
        self.name = name
        self.num = num
        self.price = price

    # 定义成员方法
    def pristr(self):
        return ";产品ID{},产品名称{},产品数量{},产品价格{}".format(self.id, self.name, self.num, self.price)


# 定义Stock类
class Stock():
    # 创建一个空列表
    goods = []

    # 添加产品，Stock实例方法
    def add(self, product):
        # goods中有库存
        if len(self.goods) > 0:
            flag = 0
            for i in range(len(self.goods)):
                if (self.goods[i].id == product.id):
                    self.goods[i].num += product.num
                    flag = 1
                    break
                if (flag == 0):
                    self.goods.append(product)
        # goods中无库存
        else:
            self.goods.append(product)
        print(";你添加的物品信息如下:")
        print(product.pristr())

    @staticmethod
    def searchid(id):
        flag = 0
        for i in range(len(Stock.goods)):
            if (Stock.goods[i].id == id):
                flag = 1
        return flag

    @staticmethod
    def searchname(name):
        flag = 0
        for i in range(len(Stock.goods)):
            if (Stock.goods[i].name == name):
                flag = 1
        return flag

    def changestockinfo(self, id, num):
        for i in range(len(self.goods)):
            if (self.goods[i].id == id):
                if (int(self.goods[i].num) >= num):
                    self.goods[i].num = int(self.goods[i].num) - num
                else:
                    print(";库存不够，目前库存数量为{}".format(self.goods[i].num))

    def changeproinfo(self, id, name, price):
        for i in range(len(self.goods)):
            if (self.goods[i].id == id):
                if (name != ';\;n'):
                    self.goods[i].name = name
                if (price != ';\;n'):
                    self.goods[i].price = price

    def List(self, **kwargs):
        for k, w in kwargs.items():
            if (k == ";name"):
                for i in range(len(self.goods)):
                    if (self.goods[i].name == w):
                        print(";你查询的单品信息如下：")
                        print(';产品ID:%s | 产品名称: %s|产品数量: %s|产品价格:%s' % (
                            self.goods[i].id, self.goods[i].name, self.goods[i].num, self.goods[i].price))
                    elif (k == ';id'):
                        for i in range(len(self.goods)):
                            if (self.goods[i].id == w):
                                print(";你查询的单品信息如下：")
                                print(';产品ID:%s | 产品名称: %s|产品数量: %s|产品价格:%s' % (
                                    self.goods[i].id, self.goods[i].name, self.goods[i].num, self.goods[i].price))

        def List_all(self):
            n = 0
            c = 0
            print(";库存中所有产品信息如下：")
            for i in range(len(self.goods)):
                n += int(self.goods[i].num)
                c += int(self.goods[i].num) * int(self.goods[i].price)
