# eng_requisitos

A CrewAI project using JSON-first configuration.

## Prerequisites

Make sure you have Python (3.10 or higher) installed on your system.

## How to Run

Follow these steps in your terminal to set up the virtual environment, install dependencies, and run your crew:

### 1. Create and activate the virtual environment (`venv`)
```
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install tools & dependencies
```
pip install crewai crewai-tools
pip install -r requirements.txt
```

### 3. Create a .env
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run Crew
```
crewai run
```
