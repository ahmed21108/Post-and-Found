import streamlit as st
import sqlite3
import os

# -----------------------------------------
# DATABASE SETUP
# -----------------------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    # create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # create posts table
    c.execute('''
        CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            status TEXT,
            phone TEXT,
            image_path TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# -----------------------------------------
# USER AUTH FUNCTIONS
# -----------------------------------------
def signup_user(username, password):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False


def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    data = c.fetchone()
    conn.close()
    return data


# -----------------------------------------
# STREAMLIT UI
# -----------------------------------------
st.title(" Post and Found App")

menu = ["Login", "Sign Up", "Add Post", "Posts"]
choice = st.sidebar.selectbox("Pages", menu)

# -----------------------------------------
# SIGN UP PAGE
# -----------------------------------------
if choice == "Sign Up":
    st.header("Create a new account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if not username.strip() or not password.strip():
            st.error("Fill all fields!")
        else:
            created = signup_user(username.strip(), password.strip())
            if created:
                st.success("Account created successfully! You can login now.")
            else:
                st.error("Username already exists!")

# -----------------------------------------
# LOGIN PAGE
# -----------------------------------------
elif choice == "Login":
    st.header("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username.strip() or not password.strip():
            st.error("Fill all fields!")
        else:
            user = login_user(username.strip(), password.strip())
            if user:
                st.success("Logged in successfully!")
            else:
                st.error("Wrong username or password")

# -----------------------------------------
# ADD POST PAGE
# -----------------------------------------
elif choice == "Add Post":
    st.header("Add a New Post")

    title = st.text_input("Title")
    description = st.text_area("Description")
    status = st.selectbox("Status", ["Lost", "Found"])
    phone = st.text_input("Contact Phone")
    image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if st.button("Add Post"):
        if not title.strip() or not description.strip() or not phone.strip():
            st.error("Fill all fields!")
        else:
            image_path = None
            if image:
                if not os.path.exists("uploads"):
                    os.makedirs("uploads")

                image_path = f"uploads/{image.name}"
                with open(image_path, "wb") as f:
                    f.write(image.getbuffer())

            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("INSERT INTO posts(title, description, status, phone, image_path) VALUES(?, ?, ?, ?, ?)",
                      (title, description, status, phone, image_path))
            conn.commit()
            conn.close()

            st.success("Post added successfully!")

# -----------------------------------------
# POSTS PAGE
# -----------------------------------------
elif choice == "Posts":
    st.header("All Posts")

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM posts")
    posts = c.fetchall()
    conn.close()

    for post in posts:
        st.subheader(post[1])
        st.write(post[2])
        st.write("Status:", post[3])
        st.write("Phone:", post[4])
        if post[5]:
            st.image(post[5])
        st.markdown("---")
