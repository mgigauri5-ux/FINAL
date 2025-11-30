
print("ფინალური დავალება 4")

# წიგნების მართვის კონსოლ აპლიკაცია


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # წიგნის ფორმატი

    def __str__(self):
        return f"{self.title} — {self.author} ({self.year})"

    
class BookManager:

    def __init__(self):
       
        self.books = [] #ინახება მეხსიერებაში
    

    # წიგნის დამატება

    def add_book(self, book):
        self.books.append(book)
    
        print(" წიგნი დაემატა!")

    # ყველა წიგნის ჩვენება

    def list_books(self):
        if not self.books:
            print(" წიგნების სია არ არის ")
            return

        print("\n ყველა წიგნი:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")

    # წიგნის ძებნა სათაურით

    def search_by_title(self, title):
        title = title.lower()
        results = [b for b in self.books if title in b.title.lower()]

        if results:
            print("\n ნაპოვნი წიგნები:")
            for book in results:
                print(book)
        else:
            print("წიგნი ვერ მოიძებნა.")



def input_year():
    
    while True:
        year = input("გამოცემის წელი: ")
        if year.isdigit() and 0 < int(year) <= 2025:
            return int(year)
        else:
            print(" გთხოვთ შეიყვანოთ სწორი წელი!")

#ძირითადი მენიუ

def main():
    manager = BookManager()

    while True:
        print("\n====== წიგნების მართვის კონსოლი ======")
        print("1. ახალი წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სათაურით")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპერაცია: ")

        if choice == "1":
            print("\n ახალი წიგნი:")
            title = input("სათაური: ").strip()
            author = input("ავტორი: ").strip()
            year = input_year()

            book = Book(title, author, year)
            manager.add_book(book)

        elif choice == "2":
            manager.list_books()

        elif choice == "3":
            search_title = input("შეიყვანეთ საძიებო სიტყვა: ")
            manager.search_by_title(search_title)

        elif choice == "4":
            print("გამოსვლა.")
            break

        else:
            print(" არასწორი არჩევანი, სცადეთ თავიდან!")


# პროგრამის გაშვება

if __name__ == "__main__":
    main()    
