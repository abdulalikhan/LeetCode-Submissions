class Cashier(object):

    def __init__(self, n, discount, products, prices):
        self.currentInd = 0
        self.n = n
        self.discount = discount
        self.priceDict = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product, amount):
        bill = 0
        for j in range(0, len(product)):
            bill += amount[j]*self.priceDict[product[j]]
        self.currentInd += 1
        if self.currentInd == self.n:
            bill = bill * ((100-self.discount)/float(100))
            self.currentInd = 0
        return bill
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)