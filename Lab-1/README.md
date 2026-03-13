# Lab 1, Environment Setup and Your First AI Application

**Course:** CS-AI-2025, Building AI-Powered Applications  
**Week:** 1 of 15  
**Date:** Friday, March 13, 2026  
**Group A:** 09:00 to 11:00  
**Group B:** 11:00 to 13:00  
**Location:** Computer Science Lab, Kutaisi International University  
**Instructor:** Professor Zeshan Ahmad  

---

## Lab Purpose

This lab has one job. Get every student to a working local AI development setup and a successful live API call.

By the end of the session, each student should be able to:

- run Python locally
- load an API key from a `.env` file
- call a language model from code
- inspect the response
- record token usage, latency, and paid-tier cost equivalent

This is an **individual lab**.

## What Is Due This Week

### Graded
- **Homework 1, individual**
- file: `homework/hw1-individual.md`

### Not graded in Lab 1
- team contract
- team repo setup
- brainstorming templates
- problem selection
- idea evaluation against filters

Those topics belong to a later lab, not this one.

---

## What You Will Do in the Lab

You will complete three steps:

### Part 1, Setup
- check Python, Git, and editor setup
- create a Gemini API key
- create a `.env` file
- confirm `.gitignore` protects secrets

### Part 2, First Working Calls
- run the hello script
- run the prompt patterns script
- compare outputs

### Part 3, Cost and Token Awareness
- run the token counter
- log token counts and latency
- understand what a paid-tier equivalent cost would look like

---

## What You Will Not Do in This Lab

Do not spend time on these during Lab 1:

- team formation
- team contract writing
- problem brainstorming
- capstone selection
- manual rebuild reflection from a different week
- any file that is not listed in the "Use This Week" section below

That keeps the lab clean and prevents students from wandering into unrelated material.

---

## Use This Week

These are the files students should use now.

### Start here
- `README.md`, this file
- `quickstart.md`, fastest route to a working setup
- `tools-setup.md`, full installation guide if your machine is not ready

### Core lab files
- `examples/starter-code/01_hello_gemini.py`
- `examples/starter-code/02_prompt_patterns.py`
- `examples/starter-code/03_token_counter.py`

### Supporting guides
- `guides/gemini-setup-guide.md`
- `guides/prompt-engineering-101.md`
- `guides/token-and-cost-guide.md`

### Templates used for this lab or homework
- `templates/prompt-log-template.md`
- `templates/cost-tracker-template.md`
- `templates/reflection-template.md`

### Graded homework
- `homework/hw1-individual.md`

### Grading
- `grading-rubric.md`

---

## Present in This Folder, But Not Part of Lab 1

These files are visible in the folder, but students should ignore them for this week:

- `templates/team-contract.md`
- `templates/problem-template.md`
- `examples/brainstorm-example.md`
- `guides/4-filters-reference.md`
- `guides/AI-Capabilities-Reference.md`

These belong to later teamwork, problem selection, or ideation activities.

---

## Lab Flow

### Exercise 1, Hello AI
Run the first starter script and confirm that the API key works.

**Output target**
- model returns text
- token usage displays
- latency displays

### Exercise 2, Prompt Patterns
Run the prompt-pattern script and compare at least a few prompt styles.

**Output target**
- more than one prompt structure tested
- outputs differ in a visible way
- prompts are logged clearly

### Exercise 3, Token and Cost Tracker
Run the token counter and record cost and latency cleanly.

**Output target**
- token counts captured
- cost table started
- student understands where the numbers come from

---

## Redone Lab Schedule

### Group A, 09:00 to 11:00
- 09:00 to 09:10, entry, machine check, setup triage
- 09:10 to 09:20, lab overview and file map
- 09:20 to 09:40, environment setup and API key setup
- 09:40 to 10:00, Exercise 1, first API call
- 10:00 to 10:30, Exercise 2, prompt patterns
- 10:30 to 10:40, short break and troubleshooting
- 10:40 to 10:55, Exercise 3, token and cost tracker
- 10:55 to 11:00, homework briefing and exit check

### Group B, 11:00 to 13:00
- 11:00 to 11:10, entry, machine check, setup triage
- 11:10 to 11:20, lab overview and file map
- 11:20 to 11:40, environment setup and API key setup
- 11:40 to 12:00, Exercise 1, first API call
- 12:00 to 12:30, Exercise 2, prompt patterns
- 12:30 to 12:40, short break and troubleshooting
- 12:40 to 12:55, Exercise 3, token and cost tracker
- 12:55 to 13:00, homework briefing and exit check

---

## Exit Checklist

Before leaving the lab, every student should have:

- a working Python environment
- `google-genai` installed
- `python-dotenv` installed
- a valid `.env` file with `GEMINI_API_KEY`
- `.env` listed in `.gitignore`
- at least one successful live API response
- starter scripts visible and runnable
- the homework file opened and understood

If any one of these is missing, the student is not done.

---

## Homework Summary

Homework 1 is individual.

Students must submit work in their own GitHub repository, not a team repository.

Minimum submission contents:

```text
hw01/
├── README.md
├── your_script.py
└── .env.example

See homework/hw1-individual.md for the full specification.

Due: Friday, March 20, 2026, before the student's Lab 2 session.

One-Line Rule for Students

In Lab 1, do the setup, run the scripts, complete the individual homework, and ignore the team files.


## 3. Replace `Lab-1/quickstart.md`

```md
# Lab 1 Quickstart

This guide gets you from zero to a working AI API call as fast as possible.

Use this file if:

- Python is already installed
- Git is already installed
- you are comfortable with terminal commands

If not, stop and use `tools-setup.md`.

---

## What This Quickstart Covers

You will:

1. clone the correct classroom repo
2. enter the Lab 1 folder
3. create a virtual environment
4. install the required packages
5. create a `.env` file
6. run the starter scripts

This quickstart is for **Lab 1 only**.

---

## Step 1, Clone the Correct Repo

Open a terminal and run:

```bash
git clone https://github.com/ZA-KIU-Classroom/AI-POWERED-SOFTWARE-DEV-SP26.git
cd AI-POWERED-SOFTWARE-DEV-SP26/Lab-1
