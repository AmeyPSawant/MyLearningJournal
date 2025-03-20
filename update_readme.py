import os

# Paths
COURSES_DIR = "Courses"
MAIN_README = "README.md"

def generate_course_links():
    """Generate a list of course links."""
    course_links = []
    for course_name in sorted(os.listdir(COURSES_DIR)):
        course_path = os.path.join(COURSES_DIR, course_name)
        if os.path.isdir(course_path):
            readme_path = os.path.join(course_path, "README.md")
            if os.path.exists(readme_path):
                course_links.append(f"- [{course_name}]({readme_path})")
    return course_links

def update_main_readme(course_links):
    """Update the main README.md file with the list of course links."""
    with open(MAIN_README, "w") as file:
        file.write("# Course Repository\n\n")
        file.write("Welcome to my course repository! Below is a list of all the courses I am studying:\n\n")
        file.write("\n".join(course_links))
        file.write("\n")

if __name__ == "__main__":
    # Generate course links
    course_links = generate_course_links()
    
    # Update the main README.md
    update_main_readme(course_links)
    
    print("README.md updated successfully!")