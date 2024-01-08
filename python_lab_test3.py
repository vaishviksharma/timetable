# LIBRARY DATABASE
d=[]
def add_book():

    book_id=int(input("enter the Book ID :"))
    title=input("Enter the title of the book :")
    author=input("Enter the author of the book :")
    genre=input("Enter the genre/category/theme of the book :")
    av_copy=int(input("enter the avaialble copies for this book :"))

    b={
        "book_id":book_id,
        "title":title,
        "author":author,
        "genre":genre,
        "av_copy":av_copy,
    }
    d.append(b)
    print(f"New Book : {title} added successfully")


def retrieve_info():
    id=int(input("Enter the id of the book : " ))
    for i in d:
        if i["book_id"]==id:
            print(f"{i['title']} book details :\n")
            print("book ID :",i['book_id'])
            print("title :",i['title'])
            print("author :",i['author'])
            print("genre :",i['genre'])
            print("av_copy :",i['av_copy'],"\n")


def update():
    id=int(input("Enter the id of the book : " ))
    for i in d:
        if i["book_id"]==id:
            i["av_copy"]=int(input("Enter new no. of available copies : "))
    print(f"\n Available copies for {i['title']} updated successfully")


def display():
    for i in d:
        print(f"{i['title']} book details :\n")
        print("book ID :",i['book_id'])
        print("title :",i['title'])
        print("author :",i['author'])
        print("genre :",i['genre'])
        print("av_copy :",i['av_copy'],"\n")

while True:

    print("1.add new book")
    print("2.Retrieve Book information")
    print("3.update the Available copies of a book")
    print("4.Display information of all books")
    print("5.Exit the program\n")
    ch=int(input("Enter your choice (1-5): "))

    if ch==1:
        add_book()

    elif ch==2:
        retrieve_info()

    elif ch==3:
        update()

    elif ch==4:
        display()   

    elif ch==5:
        print("you quit the program")
        break
    else:
        print("That's an Invalid choice")

    
	
       
   
    
                                              

                                              



    



            






