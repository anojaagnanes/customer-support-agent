# customer-support-agent

GitAgent project for customer support AI.

---

## Project Overview

This project implements a **GitAgent-powered AI agent** to handle customer support tasks, including greeting users, responding to common FAQs, and troubleshooting issues. All agent definitions, skills, and workflows are version-controlled using Git.

---

## Features

- **Skills**:
  - `hello-world` – Basic greeting skill
  - `greet` – Personalized greetings
  - `faq` – Answer frequently asked questions
  - `troubleshoot` – Guide users through common problems

- **Workflow**:
  - Deterministic execution of skills in order: `greet → hello-world → faq → troubleshoot`
  - Error handling notifications for failed steps

- **Agent Definition**:
  - Configured in `agent.yaml` with model preferences, skills, and runtime settings
  - Workflow defined in `workflows/customer-support.yaml`
  - Skill files in `skills/` folder

- **Version Control**:
  - All changes tracked with Git for full audit and history
  - GitHub repository for remote collaboration

---

## Quick Start

### Clone the repository

```bash
git clone https://github.com/anojaagnanes/customer-support-agent.git
cd customer-support-agent
