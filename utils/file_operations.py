import os
from pathlib import Path

# Assuming the Notes directory is in the project root
NOTES_DIR = Path("Notes")

def read_note_file(folder, filename):
    """
    Read a note file from the specified folder in the Notes directory.
    
    :param folder: The folder name (e.g., "1 - Rough Notes")
    :param filename: The name of the file to read (including .md extension)
    :return: The contents of the file as a string, or None if the file doesn't exist
    """
    file_path = NOTES_DIR / folder / filename
    if file_path.exists() and file_path.is_file():
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    return None

def create_note_file(folder, filename, content):
    """
    Create a new note file in the specified folder in the Notes directory.
    This function should only be used by the Organizer agent.
    
    :param folder: The folder name (e.g., "6 - Full Notes")
    :param filename: The name of the file to create (including .md extension)
    :param content: The content to write to the file
    :return: True if the file was created successfully, False otherwise
    """
    file_path = NOTES_DIR / folder / filename
    
    # Ensure the directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    if not file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    return False

def update_note_file(folder, filename, content):
    """
    Update an existing note file in the specified folder in the Notes directory.

    :param folder: The folder name (e.g., "6 - Full Notes")
    :param filename: The name of the file to update (including .md extension)
    :param content: The new content to write to the file
    :return: True if the file was updated successfully, False otherwise
    """
    file_path = NOTES_DIR / folder / filename
    
    if file_path.exists() and file_path.is_file():
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    return False

def list_notes(folder):
    """
    List all markdown files in the specified folder.
    
    :param folder: The folder name (e.g., "1 - Rough Notes")
    :return: A list of filenames in the folder
    """
    folder_path = NOTES_DIR / folder
    if folder_path.exists() and folder_path.is_dir():
        return [f.name for f in folder_path.glob("*.md")]
    return []

def search_notes(folder, query):
    """
    Search for notes in the specified folder that contain the query string.

    :param folder: The folder name (e.g., "6 - Full Notes")
    :param query: The search query string
    :return: A list of filenames that match the query
    """
    folder_path = NOTES_DIR / folder
    matching_files = []
    if folder_path.exists() and folder_path.is_dir():
        for file in folder_path.glob("*.md"):
            content = read_note_file(folder, file.name)
            if content and query.lower() in content.lower():
                matching_files.append(file.name)
    return matching_files
