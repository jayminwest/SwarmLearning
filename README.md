## Installing Swarm:

pip install git+https://github.com/openai/swarm.git

# Knowledge Management Swarm

Welcome to the **Knowledge Management Swarm**, a sophisticated system designed to manage and organize your Zettelkasten markdown notes using AI-driven agents. This project leverages the power of OpenAI's Swarm library to create a swarm of specialized agents that collaboratively handle various aspects of knowledge management, ensuring efficient organization, retrieval, and learning from your notes.

## Table of Contents
- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Core Components](#core-components)
  - [Agents](#agents)
    - [Delegator](#delegator)
    - [Organizer](#organizer)
    - [Collector](#collector)
    - [Teacher](#teacher)
  - [Utilities](#utilities)
- [Functionality](#functionality)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Knowledge Management Swarm is built around the Zettelkasten method, a system for organizing and interlinking notes to enhance creativity and learning. The project utilizes a swarm of agents, each with distinct responsibilities, to automate the management of notes across various stages—from collection and organization to facilitating learning.

## Directory Structure

```
├── agents
│   ├── __init__.py
│   ├── collector.py
│   ├── delegator.py
│   ├── organizer.py
│   ├── teacher.py
│   └── functions
│       └── universal_functions.py
├── utils
│   ├── __init__.py
│   ├── agent_utils.py
│   ├── file_operations.py
│   └── swarm_utils.py
├── Notes
│   ├── 1 - Rough Notes
│   ├── 2 - Source Material
│   ├── 3 - Tags
│   ├── 4 - Indexes
│   ├── 5 - Templates
│   ├── 6 - Full Notes
│   └── 7 - Planning
├── run.py
├── README.md
└── .gitignore
```

## Core Components

### Agents

The project defines a set of agents, each responsible for specific tasks within the knowledge management workflow. All agents inherit from the `Agent` class provided by the `swarm` library and operate collaboratively to ensure seamless note management.

#### Delegator

- **File:** `agents/delegator.py`
- **Role:** Acts as the central coordinator of the swarm.
- **Responsibilities:**
  - Receives all user inputs and queries.
  - Determines the nature of each request.
  - Assigns tasks to the appropriate agents (Teacher, Organizer, Collector).
  - Communicates exclusively with other agents, not performing tasks directly.

**Key Features:**
- Utilizes functions to transfer tasks to other agents (`transfer_to_teacher`, `transfer_to_organizer`, `transfer_to_collector`).
- Maintains awareness of the directory structure for effective task delegation.

#### Organizer

- **File:** `agents/organizer.py`
- **Role:** Structures and categorizes the user's Zettelkasten markdown notes.
- **Responsibilities:**
  - Manages unique IDs for notes.
  - Links related notes.
  - Handles tags from the "3 - Tags" directory.
  - Assigns notes to appropriate folders based on content.

**Key Features:**
- Accesses and creates note files using functions like `read_note_file` and `create_note_file`.
- Familiar with all directories within the `Notes` folder to ensure proper categorization.

#### Collector

- **File:** `agents/collector.py`
- **Role:** Ingests and collects user information into Zettelkasten markdown notes.
- **Responsibilities:**
  - Handles data entry from "1 - Rough Notes" and "2 - Source Material".
  - Performs metadata tagging.
  - Parses content from various inputs (text, PDFs, media).
  - Converts inputs into structured markdown in "6 - Full Notes".
  - Assigns unique IDs to new notes and links them to existing ones.

**Key Features:**
- Utilizes functions like `read_note_file` and `list_notes` to manage note files effectively.

#### Teacher

- **File:** `agents/teacher.py`
- **Role:** Assists the user in internalizing and learning from their markdown notes.
- **Responsibilities:**
  - Creates learning plans based on content from "6 - Full Notes".
  - Generates quizzes and flashcards for key concepts.
  - Extracts key concepts from "Main Notes" and relevant tags.

**Key Features:**
- Leverages functions like `read_note_file` and `list_notes` to access and utilize note content for educational purposes.

### Utilities

#### File Operations

- **File:** `utils/file_operations.py`
- **Purpose:** Handles all file-related operations within the `Notes` directory.
- **Key Functions:**
  - `read_note_file(folder, filename)`: Reads the contents of a specific note.
  - `create_note_file(folder, filename, content)`: Creates a new note file in the specified folder.
  - `list_notes(folder)`: Lists all markdown files in the specified folder.

#### Swarm Utilities

- **File:** `utils/swarm_utils.py`
- **Purpose:** Provides helper functions for interacting with the swarm and processing responses.
- **Key Functions:**
  - `pretty_print_messages(messages)`: Formats and displays messages from agents.
  - `process_and_print_streaming_response(response)`: Handles and displays streaming responses from the swarm.

#### Agent Utilities

- **File:** `utils/agent_utils.py`
- **Purpose:** Converts function definitions to schemas compatible with the swarm framework.
- **Key Functions:**
  - `function_to_schema(func)`: Transforms a Python function into a schema dictionary, mapping parameter types appropriately.

## Functionality

- **Agent Communication:** Agents communicate through defined transfer functions, ensuring tasks are delegated without overlap or redundancy.
- **Note Management:** The system categorizes notes into predefined directories, maintaining a structured and easily navigable knowledge base.
- **Learning Assistance:** The Teacher agent facilitates learning by generating study materials like quizzes and flashcards based on the user's notes.
- **User Interaction:** Users interact with the system via a command-line interface provided by `run.py`, where they can input queries and receive responses from the swarm.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/knowledge-management-swarm.git
   cd knowledge-management-swarm
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Then, install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If `requirements.txt` is not present, install the Swarm library directly:*
   ```bash
   pip install git+https://github.com/openai/swarm.git
   ```

3. **Configure Environment:**
   - Create a `.env` file in the root directory to store environment variables like API keys.
   - Ensure the `Notes` directory structure is intact as per the project requirements.

4. **Initialize Swarm:**
   The `run.py` script initializes the swarm with the Delegator agent and sets up the interaction loop.

## Usage

Run the main script to start interacting with the Knowledge Management Swarm:

```bash
python run.py
```

- **Commands:**
  - **Interact:** Type your queries or inputs when prompted.
  - **Exit:** Type `exit` to terminate the chat session.

**Example Interaction:**
```
Welcome to the Knowledge Management Swarm Chat!
You can interact with various agents to manage your Zettelkasten notes.
Type 'exit' to end the chat.
==================================================
User: Add a new note about machine learning fundamentals.
[Delegator]: Task delegated to Organizer.
==================================================
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m "Add your feature"
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request**

Please ensure that your code follows the project's coding standards and that all tests pass.

## License

This project is licensed under the [MIT License](LICENSE).
