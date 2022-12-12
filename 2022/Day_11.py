class Monkey:
    items = []
    oper = None
    oper_value = None
    test_value = None
    rtrue = None
    rfalse = None

    def __init__(self, items, oper, oper_value, test_value, rtrue=None, rfalse=None):
        self.items = items
        self.oper = oper
        self.oper_value = oper_value
        self.rtrue = rtrue
        self.rfalse = rfalse
        self.test_value = test_value
        self.inspect = 0

    def get_bored(self, item):
        return (item // 3)

    def test_item(self, item):
        if item % self.test_value == 0:
            self.rtrue.get(item)
        else:
            self.rfalse.get(item)

    def modify_worry(self, item):
        if self.oper == 'mul':
            if self.oper_value == 'old':
                item = item * item
            else:
                item = item * self.oper_value
        else:
            if self.oper_value == 'old':
                item = item + item
            else:
                item = item + self.oper_value
        self.inspect += 1
        return item

    def process_round(self):
        # print(f'{self=}: {self.items=}')
        while len(self.items) > 0:

            item = self.items.pop(0)
            #             print(f'Procoessing {item}')
            item = self.modify_worry(item)
            #             print(f'Work level increased: {item}')
            item = self.get_bored(item)
            #             print(f'Bored {item}')
            self.test_item(item)

    def get(self, item):
        self.items.append(item)

    def set_rtrue(self, m):
        self.rtrue = m

    def set_rfalse(self, m):
        self.rfalse = m


if __name__ == '__main__':
    m0 = Monkey(items=[93, 54, 69, 66, 71], oper='mul', oper_value=3, test_value=7)
    m1 = Monkey(items=[89, 51, 80, 66], oper='mul', oper_value=17, test_value=19)
    m2 = Monkey(items=[90, 92, 63, 91, 96, 63, 64], oper='add', oper_value=1, test_value=13)
    m3 = Monkey(items=[65, 77], oper='add', oper_value=2, test_value=3)
    m4 = Monkey(items=[76, 68, 94],oper='mul', oper_value='old', test_value=2)
    m5 = Monkey(items=[86, 65, 66, 97, 73, 83],oper='add', oper_value=8, test_value=11)
    m6 = Monkey(items=[78],oper='add', oper_value=6, test_value=17)
    m7 = Monkey(items=[89, 57, 59, 61, 87, 55, 55, 88],oper='add', oper_value=7, test_value=5)

    m0.set_rtrue(m7)
    m0.set_rfalse(m1)
    m1.set_rtrue(m5)
    m1.set_rfalse(m7)
    m2.set_rtrue(m4)
    m2.set_rfalse(m3)
    m3.set_rtrue(m4)
    m3.set_rfalse(m6)
    m4.set_rtrue(m0)
    m4.set_rfalse(m6)
    m5.set_rtrue(m2)
    m5.set_rfalse(m3)
    m6.set_rtrue(m0)
    m6.set_rfalse(m1)
    m7.set_rtrue(m2)
    m7.set_rfalse(m5)

    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

    for _ in range(20):
        for m in monkeys:
            m.process_round()

inspected_no = sorted([e.inspect for e in monkeys])
#Answer 1
print(inspected_no[-2] * inspected_no[-1])
