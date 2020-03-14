class JohnList:
    def __init__(self):
        self.first_item = None

    def add(self, num):
        if self.first_item == None:
            self.first_item = JohnItem(num)
        else:
            self.first_item.addToEnd(num)


    def get(self, index):
        if self.first_item:
            return self.first_item.getNthValue(index)
        else:
            return None


    def change(self, index, value):
        self.first_item.changeNthValue(index, value)


    def delete_last(self):
        if not self.first_item:
            return
        if not self.first_item.next_item:
            self.first_item = None
        else:
            self.first_item.popItem()


    def delete(self, index):
        if self.first_item:
            if index == 0:
                if self.first_item.next_item:
                    self.first_item = self.first_item.next_item
                else:
                    self.first_item = None
            else:
                self.first_item.deleteItem(index)
        else:
            return


    def insert(self, index, value):
        self.first_item.insertItem(index, value)


class JohnItem:
    def __init__(self, item):
        self.item = item
        self.next_item = None


    def getNthValue(self, index):
        if index == 0:
            return self.item
        else:
            if self.next_item:
                return self.next_item.getNthValue(index - 1)
            else:
                return None


    def changeNthValue(self, index, value):
        if index == 0:
            self.item = value
        else:
            self.next_item.changeNthValue(index - 1, value)

    def addToEnd(self, value):
        if self.next_item == None:
            self.next_item = JohnItem(value)
        else:
            self.next_item.addToEnd(value)


    def popItem(self):
        if self.next_item.next_item == None:
            self.next_item = None
        else:
            self.next_item.popItem()


    def deleteItem(self, index):
        if index == 1:
            self.next_item = self.next_item.next_item
        else:
            self.next_item.deleteItem(index - 1)


    def insertItem(self, index, value):
        if index == 1:
            newItem = JohnItem(value)
            newItem.next_item = self.next_item
            self.next_item = newItem
        else:
            self.next_item.insertItem(index - 1, value)


def main():
    myList = JohnList()
    myList.add("Texas")
    myList.add(2)
    myList.add(3)
    myList.delete(1)
    myList.insert(1, 7)
    print(myList.get(0))
    print(myList.get(1))
    print(myList.get(2))

    print(myList)


main()
