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
            # Get all .md files in the course directory
            md_files = [f for f in os.listdir(course_path) if f.endswith(".md")]
            
            if md_files:
                # Add the course name as main list item
                course_links.append(f"* {course_name}")
                
                # Add each markdown file as a sub-item
                for file_name in sorted(md_files):
                    # Generate the relative URL for the file
                    relative_path = os.path.join(COURSES_DIR, course_name, file_name).replace("\\", "/")
                    # URL-encode the path
                    encoded_path = quote(relative_path)
                    # Ensure the path starts with ./
                    relative_url = f"./{encoded_path}"
                    # Use the file name (without .md extension) as the link text
                    file_display_name = file_name.replace(".md", "")
                    course_links.append(f"   * [{file_display_name}]({relative_url})")
    
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
    print("Generated course links:", course_links)  # Debug statement
    
    # Update the main README.md
    update_main_readme(course_links)
    
    print("README.md updated successfully!")