# 📂 CIS22C Course Structure Generator  
*A Python script to automate directory/file creation for "Sp25 CIS D022C Data Abstract & Structures" with Markdown templates.*  

> *Script developed with assistance from [DeepSeek Chat](https://deepseek.com).*


## 🚀 Purpose  
Automates the tedious process of:  
✅ Creating nested directories for weekly course materials  
✅ Generating pre-formatted Markdown files (e.g., `Lesson 9`, `Lab 10`)  
✅ Bypassing Windows' path length limits for long filenames  
✅ Adding a `TODO` tracker for assignments  

>I really have used hours modifying this project, so I want to upload it and help others saving time.
>Of course, if you have seen this :)

## ⚙️ Features  
- **Structured Templates**: Consistent headers for all files (e.g., `Class`, `Completeness`).  
- **Error Handling**: Skips files if paths are invalid and logs errors.  
- **Extended Path Support**: Uses `\\?\` prefix to avoid Windows' 260-character limit.  
- **Customizable**: Edit `template` or `todo_content` variables for different courses.  



## 🛠️ Setup  
### Requirements:  
- Python 3.6+  
- No external libraries needed.  

### Run the Script:  
```bash
python generate_course_structure.py
```
(Optional: Pass a custom root path as an argument.)

## 📂 Generated Structure
```plaintext
Week 5. Trees, Binary Trees and Binary Search Trees/
│
├── Week 5 Help and Discussion.md
├── CIS22C TODO.md
├── Lesson 9/ (Welcome, Tree ADT, Check Yourself...)
├── Chapter 9.md
├── Lab 9/ (Pre-Lab Notes, Lab 9)
└── ... (Lesson 10, Chapter 10, etc.)
```

## 🖊️ Customization
Edit the Structure mentioned above and these variables in the script:

```python
# Change course name/template
template = """---
Class: "Sp25 CIS D022C Data Abstract & Structures\\r"
---"""

# Modify the TODO table columns
todo_content = """
| Date       | Status  | Task          | Due     |
|------------|---------|---------------|---------|
"""
```

For the TODO table columns, the following is an example of what I normally use:
```
| Date       | Status                  | Task                                | Type / Points       | Due    |
| ---------- | ----------------------- | ----------------------------------- | ------------------- | ------ |
| Mon May 6  | <input type="checkbox"> | Welcome to Lesson 9!                | Page                | 9:00pm |
```


## ❓ Why This Matters
Saves Time: No more manual file/directory creation.

Consistency: Ensures all files follow the same format.

Scalable: Adaptable for future courses.

## 📜 License  
This project is licensed under the **MIT License**.  

```text
Copyright (c) 2024 [Your Name or GitHub Username]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

