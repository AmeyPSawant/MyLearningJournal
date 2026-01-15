import os
from urllib.parse import quote

# Paths
COURSES_DIR = "Courses"
MAIN_README = "README.md"

def generate_course_links():
    """Generate a hierarchical list of course links with relative URLs."""
    course_links = []
    
    for course_name in sorted(os.listdir(COURSES_DIR)):
        course_path = os.path.join(COURSES_DIR, course_name)
        if os.path.isdir(course_path):
            # Get all items in the course directory
            items = os.listdir(course_path)
            
            # Separate files and subdirectories
            files = []
            subdirs = []
            
            for item in items:
                item_path = os.path.join(course_path, item)
                if os.path.isfile(item_path) and item.endswith((".md", ".txt")) and item != "README.md":
                    files.append(item)
                elif os.path.isdir(item_path) and item != "assets":
                    subdirs.append(item)
            
            # Only add course if it has files or subdirectories
            if files or subdirs:
                # Generate the relative URL for the course directory
                course_dir_path = os.path.join(COURSES_DIR, course_name).replace("\\", "/")
                encoded_dir_path = quote(course_dir_path)
                course_dir_url = f"./{encoded_dir_path}"
                
                # Add the course name as main list item with link to directory
                # Add folder emoji before course name
                course_links.append(f"* [📁 {course_name}]({course_dir_url})")
                
                # First, add files in the root of the course directory
                for file_name in sorted(files):
                    file_path = os.path.join(course_path, file_name)
                    
                    if file_name.endswith(".md"):
                        # For .md files, link directly to the file
                        relative_path = os.path.join(COURSES_DIR, course_name, file_name).replace("\\", "/")
                        encoded_path = quote(relative_path)
                        relative_url = f"./{encoded_path}"
                        file_display_name = file_name.replace(".md", "")
                        course_links.append(f"  * [{file_display_name}]({relative_url})")
                    
                    elif file_name.endswith(".txt"):
                        # For .txt files, read the content and use it as a link
                        try:
                            with open(file_path, "r", encoding="utf-8") as txt_file:
                                content = txt_file.read().strip()
                                
                            if content:
                                file_display_name = file_name.replace(".txt", "")
                                course_links.append(f"  * <a href=\"{content}\" target=\"_blank\">{file_display_name}</a>")
                            else:
                                file_display_name = file_name.replace(".txt", "")
                                course_links.append(f"  * {file_display_name}")
                                
                        except Exception as e:
                            file_display_name = file_name.replace(".txt", "")
                            course_links.append(f"  * {file_display_name}")
                
                # Then, add subdirectories
                for subdir_name in sorted(subdirs):
                    subdir_path = os.path.join(course_path, subdir_name)
                    
                    # Check if README.md exists in the subdirectory
                    readme_path = os.path.join(subdir_path, "README.md")
                    has_readme = os.path.isfile(readme_path)
                    
                    if has_readme:
                        # Link to the README.md file
                        relative_path = os.path.join(COURSES_DIR, course_name, subdir_name, "README.md").replace("\\", "/")
                        encoded_path = quote(relative_path)
                        relative_url = f"./{encoded_path}"
                        # Add folder emoji before subfolder name
                        course_links.append(f"  * [📁 {subdir_name}]({relative_url})")
                    else:
                        # Link to the subdirectory
                        subdir_relative_path = os.path.join(COURSES_DIR, course_name, subdir_name).replace("\\", "/")
                        encoded_subdir_path = quote(subdir_relative_path)
                        subdir_url = f"./{encoded_subdir_path}"
                        # Add folder emoji before subfolder name
                        course_links.append(f"  * [📁 {subdir_name}]({subdir_url})")
                    
                    # Get files in the subdirectory
                    subdir_files = [f for f in os.listdir(subdir_path) 
                                   if os.path.isfile(os.path.join(subdir_path, f)) 
                                   and f.endswith((".md", ".txt"))
                                   and f != "README.md"]  # Exclude README.md from the file list
                    
                    # Add files from subdirectory
                    for file_name in sorted(subdir_files):
                        file_path = os.path.join(subdir_path, file_name)
                        
                        if file_name.endswith(".md"):
                            relative_path = os.path.join(COURSES_DIR, course_name, subdir_name, file_name).replace("\\", "/")
                            encoded_path = quote(relative_path)
                            relative_url = f"./{encoded_path}"
                            file_display_name = file_name.replace(".md", "")
                            # Files don't get emoji, just plain links
                            course_links.append(f"    * [{file_display_name}]({relative_url})")
                        
                        elif file_name.endswith(".txt"):
                            try:
                                with open(file_path, "r", encoding="utf-8") as txt_file:
                                    content = txt_file.read().strip()
                                    
                                if content:
                                    file_display_name = file_name.replace(".txt", "")
                                    course_links.append(f"    * <a href=\"{content}\" target=\"_blank\">{file_display_name}</a>")
                                else:
                                    file_display_name = file_name.replace(".txt", "")
                                    course_links.append(f"    * {file_display_name}")
                                    
                            except Exception as e:
                                file_display_name = file_name.replace(".txt", "")
                                course_links.append(f"    * {file_display_name}")
    
    return course_links

def update_main_readme(course_links):
    """Update the main README.md file with the list of course links."""
    with open(MAIN_README, "w", encoding="utf-8") as file:
        file.write("# My Learning Journal\n\n")
        file.write("Welcome to my course repository! Below is a list of all the courses I am studying:\n\n")
        file.write("\n".join(course_links))
        file.write("\n")

if __name__ == "__main__":
    # Generate course links
    course_links = generate_course_links()
    print("Generated course links:")
    for link in course_links:
        print(link)
    
    # Update the main README.md
    update_main_readme(course_links)
    
    print("\nREADME.md updated successfully!")