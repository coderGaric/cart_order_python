class Cart:
    def __init__(self, name):
        self._name = name
        self._basket = []

    def __len__(self):
        return len(self._basket)

    def __str__(self):
        return f"{self._name} have {len(self._basket)} items in the basket"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def cart(self):
        return {
            "name": self.name,
            "basket": self._basket
        }
        
    def add(self, item):
        self._basket.append(item)

    def __getitem__(self, index):
        return self._basket[index]

    def __setitem__(self, index, new_item):
        self._basket[index] = new_item

    def __delitem__(self, index):
        del self._basket[index]

