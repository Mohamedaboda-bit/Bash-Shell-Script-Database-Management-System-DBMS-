<<<<<<< HEAD
# Database Management System (DBMS) - Bash Script Project  
=======
# Database Management System (DBMS) - Bash Script with GUI  
>>>>>>> 111f187 (added GUI)
**Team Members**: Mohamed Abdel Aal, Nada Salah  

---

## Overview  
<<<<<<< HEAD
This project is a command-line Database Management System (DBMS) implemented in Bash. It allows users to manage databases and tables with operations like creation, deletion, insertion, updates, and queries. The system operates at two levels:  
1. **Database Level**: Create, list, use, or drop entire databases.  
2. **Table Level**: Within a database, manage tables and perform CRUD operations.  
=======
This project is a **Graphical Database Management System (DBMS)** that provides an interactive way to manage databases and tables. The system allows users to **create, delete, update, and query** databases and tables using a Bash backend with a Python GUI.  
>>>>>>> 111f187 (added GUI)

---

## Features  

### **Database-Level Operations**  
- **Create Database**: Create a new database with a valid name.  
- **List Databases**: Display all existing databases.  
- **Use Database**: Select a database to perform table operations.  
- **Drop Database**: Delete an entire database.  

### **Table-Level Operations**  
- **Create Table**: Define tables with columns and data types (Integer/String).  
- **Drop Table**: Delete a table.  
- **Insert Data**: Add records to a table with type validation.  
- **Delete Data**: Remove records (all or condition-based).  
- **Update Data**: Modify existing records based on conditions.  
- **Select Data**: Query data using selection, projection, or display all records.  

---

<<<<<<< HEAD
## File Structure  
### **Database-Level Scripts**  
- **mainMenu.txt**: Main menu for database operations (create, use, list, drop).  
- **create.txt**: Creates a new database.  
- **drop.txt**: Deletes a database.  
- **use.txt**: Selects a database to enter table operations submenu.  

### **Table-Level Scripts**  
- **submenu.txt**: Submenu for table operations (create, insert, delete, etc.).  
- **create.txt**: Creates a table with columns and data types.  
- **drop.txt**: Deletes a table.  
- **insert.txt**: Inserts data into a table with validation.  
- **delete.txt**: Deletes records from a table.  
- **update.txt**: Updates records conditionally.  
- **select.txt**: Queries data from a table.  
- **validdatorFunction.txt**: Validates data types during insertion.  
- **createHelperFunctions.txt**: Helper functions for table creation.  

### **Utility Scripts**  
- **entryPoint.txt**: Initializes the DBMS environment and starts the main menu.  

---

## Usage  

### **1. Starting the DBMS**  
Run the entry point script:  
```bash
./entryPoint.txt
=======
## Setup Instructions  

### **1️⃣ Install Dependencies**  
Before running the project, you need to set up a **virtual environment** and install the required Python modules.  

Run the following commands:  

```bash
# Create and activate a virtual environment
python -m venv .venv

# Activate virtual environment (MacOS/Linux)
source .venv/bin/activate  

# Activate virtual environment (Windows)
.venv\Scripts\activate  

# Install required dependencies
pip install -r requirements.txt
>>>>>>> 111f187 (added GUI)
