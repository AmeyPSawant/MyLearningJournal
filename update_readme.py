import os

# Paths
COURSES_DIR = "Courses"
MAIN_README = "README.md"

def generate_course_links():
    """Generate a list of course links with relative URLs."""
    course_links = []
    for course_name in sorted(os.listdir(COURSES_DIR)):
        course_path = os.path.join(COURSES_DIR, course_name)
        if os.path.isdir(course_path):
            # Look for .md files in the course directory
            for file_name in os.listdir(course_path):
                if file_name.endswith(".md"):
                    # Generate the relative URL for the file
                    relative_path = os.path.join(COURSES_DIR, course_name, file_name).replace("\\", "/")
                    # Ensure the path starts with ./
                    relative_url = f"./{relative_path}"
                    # Use the course name as the link text
                    course_links.append(f"- [{course_name}]({relative_url})")
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