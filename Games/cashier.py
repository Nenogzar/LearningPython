class Cashier:
    num = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 1]
    n = len(num)
    cash = [0] * n
    overall = 0

    def set_data(self, s):
        self.overall = 0
        s = s.split(',')
        for e in s:
            parts = e.split('-')
            if len(parts) == 2:
                val, cnt = map(int, parts)
                self.cash[self.num.index(val)] = cnt
                self.overall += val * cnt
            else:
                print('Invalid input format:', e)
                return

    def show_total_amount(self):
        print('Total at checkout', self.overall, 'eur.')
        for i in range(self.n - 1, -1, -1):
            if self.cash[i]:
                print(self.num[i], '-', self.cash[i])
        print()

    def sell_product(self, price, income):
        cash_buf = self.cash.copy()
        change = income - price
        if change < 0:
            print('Insufficient funds. Operation rejected.')
            print()
            return
        for i in range(self.n):
            self.cash[i] += income // self.num[i]
            income = income % self.num[i]
        change_cash = [0] * self.n
        for i in range(self.n):
            x = min(change // self.num[i], self.cash[i])
            change_cash[i] += x
            change -= x * self.num[i]
            self.cash[i] -= x
        if change:
            print('Not enough currency! The cash desk cannot issue the remaining', change, 'eur.')
            print('Top up the cash register and repeat the operation')
            print()
            self.cash = cash_buf.copy()
            return
        for i in range(self.n - 1, -1, -1):
            if change_cash[i]:
                print(self.num[i], '-', change_cash[i])
        print()


cashier = Cashier()
request = input()
while request != '0':
    if request[0] == '1':
        cashier.set_data(request[2:])
    elif request[0] == '2':
        price, income = map(int, request[2:].split())
        cashier.sell_product(price, income)
    elif request == '3':
        cashier.show_total_amount()
    else:
        print('Invalid request.')
        print()
    request = input()


#  test input
""" loading a cassette with banknotes """
#  1, 5000-10,2000-10,1000-10,500-10,200-10,100-10,50-10,10-10,5-10,1-10


"""  banknote availability check """
#  3


""" This input means that the customer buys a product at a price of €50 and pays with a €100 note/coin."""
#  2,50 100