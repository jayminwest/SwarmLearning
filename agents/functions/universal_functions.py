def transfer_to_organizer(text=""):
    from ..organizer import organizer
    return organizer    

def transfer_to_delegator(text=""):
    from ..delegator import delegator
    return delegator

def transfer_to_collector(text=""):
    from ..collector import collector
    return collector

def transfer_to_teacher(text=""):
    from ..teacher import teacher
    return teacher

def update_note_file(folder, filename, content):
    from utils.file_operations import update_note_file
    return update_note_file(folder, filename, content)

def search_notes(folder, query):
    from utils.file_operations import search_notes
    return search_notes(folder, query)

