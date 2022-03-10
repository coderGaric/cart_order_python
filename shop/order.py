from datetime import date


class Order:
    def __init__(self):
        self.date = date.today()
        self.order_list = []

    def add_order(self, order):
        self.order_list.append(order)

    def cancel_order(self, index):
        del self.order_list[index]

    def __len__(self):
        return len(self.order_list)

    def __getitem__(self, index):
        if index >= len(self.order_list):
            return "Order not found"
        order = self.order_list[index]
        self.output(index, order)
        return "Order found"

    def output_list(self):
        print(f"---- {self.date} ----")
        for index, order in enumerate(self.order_list):
            self.output(index, order)

    def output(self, i, obj):
        print(f"Order from {obj.name}:")
        for num in range(len(obj)):
            print(f"{num + 1}. {obj[num]}")

