# Database Management System (DBMS) - Bash Script with GUI  
**Team Members**: Mohamed Abdel Aal, Nada Salah  

---

## Overview  
This project is a **Graphical Database Management System (DBMS)** that provides an interactive way to manage databases and tables. The system allows users to **create, delete, update, and query** databases and tables using a Bash backend with a Python GUI.  

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
