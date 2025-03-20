import os

# Define the repository root directory
repo_root = "."

# Create or overwrite the main README.md file
with open("README.md", "w") as main_readme:
    main_readme.write("#  The Learning Lab\n\n")
    main_readme.write("## List of Courses\n\n")

    # Traverse the repository to find course folders
    for root, dirs, files in os.walk(repo_root):
        # Skip the root directory and hidden folders (like .git)
        if root == repo_root or root.startswith("."):
            continue

        # Extract the course folder name
        course_name = os.path.basename(root)

        # Check if the folder contains a README.md file
        if "README.md" in files:
            # Write a link to the course README.md file
            main_readme.write(f"- [{course_name}]({os.path.join(root, 'README.md')})\n")

print("README.md updated successfully!")