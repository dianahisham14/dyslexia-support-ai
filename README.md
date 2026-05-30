# Dyslexia Support AI

## KMK3013 Knowledge-Based System Group Assignment

### Project Description

This project implements a Dyslexia Support AI Assistant using a ReAct-based agent architecture, LangChain, and Google Gemini 2.5 Flash. The system provides dyslexia-friendly learning support through expert-derived rules and specialised intervention tools.

---

## System Requirements

* Python 3.11
* LangChain
* LangChain Google Generative AI
* Google Generative AI

---

## Installation Guide

### Step 1: Install Python 3.11

Download and install Python 3.11 from:

https://www.python.org/downloads/

### Step 2: Verify Python Installation

Open the terminal and run:

```bash
py -0
```

Expected output:

```text
Installed Pythons found:
-3.11
```

### Step 3: Open the Project Folder

Open the project folder in Visual Studio Code.

Example:

```text
dyslexia_agent
```

### Step 4: Install Required Packages

Open the terminal and navigate to the project folder:

```bash
cd "YOUR_PROJECT_FOLDER"
```

Install the required libraries:

```bash
py -3.11 -m pip install langchain
py -3.11 -m pip install langchain-google-genai
py -3.11 -m pip install google-generativeai
```

### Step 5: Verify Installed Packages

Run:

```bash
py -3.11 -m pip list
```

Verify that the following packages are installed:

```text
langchain
langchain-google-genai
google-generativeai
```

### Step 6: Run the Application

Navigate to the project directory and execute:

```bash
py -3.11 dyslexia_agent.py
```

If the system runs successfully, the terminal will display the ReAct execution trace, including:

```text
Thought:
Action:
Final Answer:
```

---

## Authors

KMK3013 Knowledge-Based System Group Assignment
