class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new): 
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):  
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[{self.book_id}] {self.title} / {self.author} / {self.year}"



class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

   
    def insert(self, book):
        new_node = Node(book)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.link:
                p = p.link
            p.append(new_node)

   
    def find_by_id(self, book_id):
        p = self.head
        while p:
            if p.data.book_id == book_id:
                return p.data
            p = p.link
        return None

   
    def find_by_title(self, title):
        p = self.head
        while p:
            if p.data.title == title:
                return p.data
            p = p.link
        return None

    
    def find_pos_by_title(self, title):
        p = self.head
        pos = 0
        while p:
            if p.data.title == title:
                return pos
            p = p.link
            pos += 1
        return -1

   
    def delete_by_title(self, title):
        if self.isEmpty():
            return False

        
        if self.head.data.title == title:
            self.head = self.head.link
            return True

        p = self.head
        while p.link:
            if p.link.data.title == title:
                p.popNext()
                return True
            p = p.link
        return False

    
    def display_all(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        p = self.head
        while p:
            print(p.data)
            p = p.link



class BookManagement:
    def __init__(self):
        self.books = LinkedList()

 
    def add_book(self, book_id, title, author, year):
        if self.books.find_by_id(book_id):
            print(" 중복된 책 번호입니다. 추가 불가.")
            return
        new_book = Book(book_id, title, author, year)
        self.books.insert(new_book)
        print(" 도서가 성공적으로 추가되었습니다.")

   
    def remove_book(self, title):
        if self.books.delete_by_title(title):
            print("도서가 삭제되었습니다.")
        else:
            print(" 해당 제목의 도서를 찾을 수 없습니다.")

    def search_book(self, title):
        book = self.books.find_by_title(title)
        if book:
            print(" 조회 결과:", book)
        else:
            print(" 해당 제목의 도서를 찾을 수 없습니다.")

    # 전체 도서 목록 출력
