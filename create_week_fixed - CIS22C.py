import os

# Template for markdown files
template = """---
Class:
  - "[Course]\\r"
Completeness:
---
#CIS22C

"""

todo_content = """---
Class:
  - "[Course]\\r"
Completeness:
---
#CIS22C

```
<input type="checkbox" checked>
```

```
<input type="checkbox" checked>
```

"""


# Directory structure in exact sequence
directories = [
    ("Week 5 Help and Discussion", [
        "Week 5 Help and Discussion.md"
    ]),
    ("Lesson 9. Trees, Binary Trees and Introduction to Binary Search Trees", [
        "Welcome to Lesson 9!.md",
        "The Tree ADT.md",
        "Check Yourself. The Tree ADT.md",
        "The Binary Tree ADT.md",
        "Check Yourself. The Binary Tree ADT.md",
        "Introduction to the Binary Search Tree ADT.md",
        "Check Yourself. Introduction to the BST ADT.md",
        "Chapter 9.md",
        "Pre-Lab 9 Helpful Notes.md",
        "Lab 9.md"    
    ]),
    ("Lesson 10. BST Search and Big-O Runtimes", [
        "Welcome to Lesson 10!.md",
        "Searching a BST.md",
        "Check Yourself. BST Search.md",
        "BST Efficiency.md",
        "Check Yourself. BST Efficiency.md",
        "Chapter 10.md",
        "Lab 10.md"
    ])
]

# Target directory path
target_dir = "./Week 5 Trees, Binary Trees and Binary Search Trees"

def make_long_path_safe(path):
    if os.name == 'nt' and not path.startswith('\\\\?\\'):
        return '\\\\?\\' + os.path.abspath(path)
    return path

target_dir = make_long_path_safe("./Week 5 Trees, Binary Trees and Binary Search Trees")
os.makedirs(target_dir, exist_ok=True)

for dir_name, files in directories:
    dir_path = make_long_path_safe(os.path.join(target_dir, dir_name))
    os.makedirs(dir_path, exist_ok=True)
    
    for filename in files:
        filepath = make_long_path_safe(os.path.join(dir_path, filename))
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(template.format(task_name=os.path.splitext(filename)[0]))
            print(f"Created: {os.path.join(dir_name, filename)}")
        except Exception as e:
            print(f"Failed: {os.path.join(dir_name, filename)}\n   Error: {str(e)}")



# Root level files
root_files = ["Week 5 Quiz.md"]


def create_directory_structure():
    # Create root directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    print(f"Root directory created/verified: {target_dir}")

    # Create all directories and their files
    for dir_name, files in directories:
        dir_path = os.path.join(target_dir, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"\nCreated directory: {dir_name}")
        
        for filename in files:
            filepath = os.path.join(dir_path, filename)
            task_name = os.path.splitext(filename)[0]
            
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(template.format(task_name=task_name))
                print(f"  Created file: {filename}")
            except Exception as e:
                print(f"  Error creating {filename}: {str(e)}")

    # Create root-level files
    print("\nCreating root-level files:")
    for filename in root_files:
        filepath = os.path.join(target_dir, filename)
        task_name = os.path.splitext(filename)[0]
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(template.format(task_name=task_name))
            print(f"  Created file: {filename}")
        except Exception as e:
            print(f"  Error creating {filename}: {str(e)}")

    # Add this right after the root_files loop but before the completion message
    try:
        with open(os.path.join(target_dir, "CIS22C TODO.md"), "w", encoding="utf-8") as f:
            f.write(todo_content)
        print("  Created file: CIS22C TODO.md")
    except Exception as e:
        print(f"  Error creating CIS22C TODO.md: {str(e)}")  

    print("\nDirectory structure creation complete!")

if __name__ == "__main__":
    create_directory_structure()
    input("\nPress Enter to exit...")  # Keeps window open when run in IDLE
