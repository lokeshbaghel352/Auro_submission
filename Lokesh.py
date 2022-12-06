from collections import defaultdict

class BookStore:
    # main class to store all the books and their details, which is a dictionary
    def _init_(self) -> None:
        self.bookstore = dict()
    
    def _addBook(self, bookname, content):
        self.bookstore[bookname] = content
    
    
class Book(BookStore):
    # class to create books and add to the bookstore
    def _init_(self, name):
        super()._init_()
        if not self._check(name):
            self._createBook(name)
        
    def _createBook(self,name):
        book = defaultdict(list)
        self.addBook.add()
        
    def _check(self, name):
        if name in Book.allBook:
            return True
        return False

    

class Order(Book):
    def _init_(self, name):
        super()._init_(name)
        self.buy = dict()
        self.sell = dict()
    
    def _readData(self,order):
        arr = order.split()
        if len(arr)==3:
            self.delOrder(arr)
        else:
            self._addOrder(arr)

# Path: main.py
    def delOrder(self,orderarr):

        #this function tries to first check for the book if present. If present, we check for order id, and then delete the particular orderid if present
        #arr = ['DeleteOrder', 'book="book-3"', 'orderId="9036"'] -- the format of orderarr
        bookname = orderarr[1].split("=").strip('"')
        if bookname not in self.bookstore:
            return 
        orderid = orderarr[2]
        bookname.remove(orderid)
        


    def _addOrder(self,orderarr):
        # arr = ['AddOrder', 'book="book-2"', 'operation="SELL"', 'price="101.00"', 'volume="87"', 'orderId="9363"'] --
        # this function tries to first check for the book if present. If present, we check for order id, and then add the particular orderid if not present
        # if present, we update the volume
        # if not present, we add the orderid and initisalise the volume
        # if the volume is 0, we delete the orderid
        # if the volume is not 0, we update the orderid
        bookname = orderarr[1].split("=")[1].strip('"')
        if bookname not in self.allBook:
