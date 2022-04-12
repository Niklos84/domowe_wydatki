import json


class Finance:
    def __init__(self):
        try:
            with open("finance.json", "r") as f:
                self.finance = json.load(f)
        except FileNotFoundError:
            self.finance = []

    def all(self):
        return self.finance

    def get(self, id):
        finance = [finance for finance in self.all() if finance['id'] == id]
        if finance:
            return finance[0]
        return []

    def create(self, data):
        self.finance.append(data)
        self.save_all()

    def save_all(self):
        with open("finance.json", "w") as f:
            json.dump(self.finance, f, default=str)

    def update(self, id, data):
        record = self.get(id)
        if record:
            index = self.finance.index(record)
            self.finance[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        record = self.get(id)
        if record:
            self.finance.remove(record)
            self.save_all()
            return True
        return False


finance = Finance()