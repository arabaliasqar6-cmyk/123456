# 40426993 
#علی اصغر عرب 
#اسم کتاب ها 
file = open("books.txt","r")
for book in file:	
	book = book.strip() 
    character=book[0]
    nom=len(book)
    print (character + str(nom))
file.close()