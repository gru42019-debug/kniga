import streamlit as st
#--------INITIAL BOOK DATABASE--------
books = [
"The Hobbit",
"1984",
"Pride and Prejudice",
"To Kill a Mockingbird",
"The Great Gatsby"
]
#--------APP TITLE--------
st.title("Book Checker App")
st.write("Enter a book title to check if it exists in the database.")
#-------USER INPUT--------
user_input = st.text_input("Book Title")
#------CHECK BUTTON--------
if st.button("Check Book"):
if user_input.strip()== "":
st.warning("Please enter a book:")
elif user_input in books:
st.success("The book exists in the database!")
else:
st.error("The book does NOT exists in the database!")



import stream as st
if "books" not in st.session_state:
  st.session_state.books = []

title = st.text_input("Заглавие")
author = st.text_input("Автор")

if st.button("Добави книга"):
  book = {
    "title":title,
    "author":author
  }
  st.session_state.books.append(book)
  st.success("Книгата е добавена!")
  st.write("### Списък с книги:")
  st.write(st.session_state.books)
import streamlit as st

st.title("Приложение")

# Създаваме масив (списък), ако още не съществува
if "books" not in st.session_state:
    st.session_state.books = []

st.header("➕ Добави книга")

title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }

    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

if st.button("Покажи всички книги"):

    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", book["price"])
            st.write("--------------------")



st.header("Търсене по автор")

search_author = st.text_input("Въведи име на автор")

if st.button("Търси по автор"):

    found = False

    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True

    if found == False:
        st.write("Няма намерени книги от този автор.")

