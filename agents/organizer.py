from swarm import Agent
from .functions.universal_functions import (
    transfer_to_delegator, 
    transfer_to_collector, 
    transfer_to_teacher,
    update_note_file,
    search_notes
)
from utils.file_operations import read_note_file, create_note_file, list_notes
from utils.agent_utils import function_to_schema
from .config import AGENT_MODEL

organizer = Agent(
    name="Organizer",
    model=AGENT_MODEL,
    instructions="""
    You are the Organizer, structuring and categorizing the user's Zettelkasten markdown notes.

    Your responsibilities:
    - Manage unique IDs for notes.
    - Link related notes.
    - Handle tags from '3 - Tags'.
    - Assign notes to appropriate folders based on content.
    - Update and delete notes as necessary.
    - Search for specific notes based on criteria.

    You should be familiar with all directories:
    - 1 - Rough Notes
    - 2 - Source Material
    - 3 - Tags
    - 4 - Indexes
    - 5 - Templates
    - 6 - Full Notes
    - 7 - Planning

    You can access and manipulate note files using these functions:
    - read_note_file(folder, filename): Read the contents of a specific note
    - create_note_file(folder, filename, content): Create a new note file
    - update_note_file(folder, filename, content): Update an existing note file
    - delete_note_file(folder, filename): Delete a note file
    - list_notes(folder): List all notes in a specific folder
    - search_notes(folder, query): Search for notes containing the query

    Example task: Assign book quotes to '2 - Source Material' under the book's title.
    """,
    functions=[transfer_to_delegator, transfer_to_collector, transfer_to_teacher, update_note_file, search_notes],
)
