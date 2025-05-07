📂 CIS22C Course Structure Generator
*A Python script to automate directory/file creation for "Sp25 CIS D022C Data Abstract & Structures" with Markdown templates.*
> *Script developed with assistance from DeepSeek Chat (https://deepseek.com).*

🚀 Purpose
Automates the tedious process of:
✅ Creating nested directories for weekly course materials
✅ Generating pre-formatted Markdown files (e.g., Lesson 9, Lab 10)
✅ Bypassing Windows' path length limits for long filenames
✅ Adding a TODO tracker for assignments

⚙️ Features
Structured Templates: Consistent headers for all files (e.g., Class, Completeness).

Error Handling: Skips files if paths are invalid and logs errors.

Extended Path Support: Uses \\?\ prefix to avoid Windows' 260-character limit.

Customizable: Edit template or todo_content variables for different courses.

🛠️ Setup
Requirements:

Python 3.6+

No external libraries needed.

Run the Script:

bash
python generate_course_structure.py
(Optional: Pass a custom root path as an argument.)

📂 Generated Structure
plaintext
Week 5. Trees, Binary Trees and Binary Search Trees/
│
├── Week 5 Help and Discussion.md
├── CIS22C TODO.md
├── Lesson 9/ (Welcome, Tree ADT, Check Yourself...)
├── Chapter 9.md
├── Lab 9/ (Pre-Lab Notes, Lab 9)
└── ... (Lesson 10, Chapter 10, etc.)
🖊️ Customization
Edit these variables in the script:

python
# Change course name/template
template = """---
Class: "Sp25 CIS D022C Data Abstract & Structures 64Z Parrish 46796\\r"
---"""

# Modify the TODO table columns
todo_content = """
| Date       | Status  | Task          | Due     |
|------------|---------|---------------|---------|
"""
❓ Why This Matters
Saves Time: No more manual file/directory creation.

Consistency: Ensures all files follow the same format.

Scalable: Adaptable for future courses (e.g., CIS22D).

📜 License
Free to use/modify! 
