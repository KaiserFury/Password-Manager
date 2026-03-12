# 🔐 Password Manager (Python Tkinter)

A simple **Password Manager application built with Python and Tkinter** that helps users generate strong passwords, store login credentials, and retrieve them easily.
The application stores data securely in a **JSON file** and includes a **password generator** for creating strong passwords using letters, numbers, and symbols.

---

# 📌 Features

* 🔑 Generate strong random passwords
* 💾 Save website login credentials
* 🔎 Search saved passwords for any website
* 📋 Automatically copy generated passwords to clipboard
* 🖥 Simple and user-friendly GUI using Tkinter
* 📂 Data stored locally using JSON

---

# 🛠 Technologies Used

* **Python**
* **Tkinter** – GUI development
* **JSON** – Data storage
* **Random** – Password generation
* **Pyperclip** – Clipboard copy functionality

---

# ⚙️ Installation

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/password-manager.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd password-manager
```

### 3️⃣ Install Required Libraries

```bash
pip install pyperclip
```

*(Tkinter usually comes pre-installed with Python.)*

### 4️⃣ Run the Program

```bash
python main.py
```

---

# 🚀 Usage

1. Enter the **Website name**.
2. Enter your **Email/Username**.
3. Click **Generate Password** to create a strong password.
4. Click **Add** to save the credentials.
5. Use the **Search button** to retrieve saved credentials for a website.

All saved credentials are stored in a file called:

```
Detail.json
```

---

# 📂 Project Structure

```
password-manager/
│
├── main.py          # Main application code
├── logo.png         # GUI logo image
├── Detail.json      # Stored credentials
└── README.md        # Project documentation
```

---



---

# 🐞 Possible Improvements

* Add **password encryption**
* Implement **master password authentication**
* Improve **UI design**
* Add **password strength indicator**
* Export/import credentials

---



# 👨‍💻 Author

Developed by **Abhishek Ranjan**
