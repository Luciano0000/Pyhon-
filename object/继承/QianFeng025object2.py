# has a
# 学生有好几本书和好几个电脑

'''
知识点:
1.has a 一个类当中使用(引用)另外一种自定义的类型
    student使用 computer book
2.类型: 系统类型(str,dict,int...)    自定义类型(自定义的类) 
        s=Student()     s就是Stundent"类型" 的对象
        
'''
class Student:  # has a 关系
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    


    def borrow_book(self, book):  # 借书
        for book1 in self.books:
            if book1.bname == book.bname:
                print('此书已经借过')
                break
        else:
            #将参数book添加到列表中
            self.books.append(book)
            print('添加成功!')

    def show_book(self):
        for book in self.books: #book就是一个book对象
            print(book.bname) #打印书名

    def __str__(self):
        return '{},{},{}'.format(self.name,self.computer,self.books)

class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname+'----'+self.author+'----'+str(self.number)


class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print('这个在使用电脑上网')

    def __str__(self):
        return self.brand+'----'+self.type+'-----'+self.color


# 创建对象
computer = Computer('惠普 ', '炫龙DD3PLUS', '黑色')
book = Book('时间简史', '霍金', 10)

stu = Student('老八', computer, book) #包含关系
print(stu)
book1=Book('鬼吹灯','天下霸唱',8)
stu.borrow_book(book1)
stu.show_book()


# book1=Book('鬼吹灯','天下霸唱',8)
# stu.borrow_book(book1)
# print('------------------------')
# stu.show_book()