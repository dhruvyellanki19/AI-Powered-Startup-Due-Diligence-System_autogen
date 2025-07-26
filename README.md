# AI-Powered Startup Due Diligence System

A modular, multi-agent pipeline for **automated startup analysis and due diligence**. This project uses **Google Gemini** (via API key), Python, and customizable agents to evaluate startups on market, product, competition, risk, tech, and more—**generating a professional due diligence report automatically**.

---

## Project Overview

This project automates the end-to-end due diligence process for startups, simulating how a VC or analyst team would evaluate a company. You provide a startup description; the system orchestrates multiple “expert” AI agents, each analyzing a specific domain, and compiles a downloadable report (Word DOCX).

**Key Features:**

* Modular agent classes for Market, Product, Tech, Risk, Competition, Investment, etc.
* Uses Google Gemini API for LLM-powered insights (bring your own key)
* Simple `run_pipeline.py` orchestrates the workflow
* Generates and saves a complete, professional due diligence report
* Easily customizable for different questions, startup types, or agent prompts

---

## Folder Structure

```text
ai_due_diligence/
├── agents/
│   ├── founder.py
│   ├── market.py
│   ├── product.py
│   ├── competitor.py
│   ├── tech.py
│   ├── risk.py
│   ├── investment.py
│   ├── synthesis.py
│   ├── writer.py
│   └── vc.py
├── inputs/
│   └── startup_description.txt
├── outputs/
│   └── startup_due_diligence_report.docx
├── llm.py
├── requirements.txt
├── run_pipeline.py
└── README.md
```

---

## Setup & Installation

1. **Clone the Repository**

   ```bash
   git clone <your-github-url>
   cd ai_due_diligence
   ```

2. **Create & Activate Virtual Environment**

   ```bash
   python3 -m venv startup_venv
   source startup_venv/bin/activate
   ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Google Gemini API Key**

   * Create a `.env` file in the root directory:

     ```
     GOOGLE_API_KEY=your-gemini-api-key
     ```
   * Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

5. **Prepare Your Startup Description**

   * Edit `inputs/startup_description.txt` with the description of the startup you want to analyze.

---

## How It Works (Workflow)

1. **Input:**
   The user provides a plain-text description of the startup in `inputs/startup_description.txt`.

2. **Pipeline Orchestration:**
   `run_pipeline.py` loads the description and triggers each specialized agent class.
   Each agent asks a domain-specific question (market, product, tech, risk, etc.), builds a prompt, and gets a detailed answer using Gemini via `llm.py`.

3. **Multi-Agent Analysis:**
   Each agent runs independently and returns its analysis.
   Example questions:

   * Market: "What is the target market size and major trends?"
   * Product: "How differentiated and scalable is the product?"
   * Risk: "What are the key risks and mitigations?"
   * Tech: "Is the tech stack robust and scalable?"
   * Competitor: "Who are the main competitors? Compare strengths/weaknesses."
   * VC: "Would you invest in this startup? Why/why not?"

4. **Synthesis & Reporting:**
   A synthesis agent combines the findings, and a report writer agent formats everything into a professional Word document.

5. **Output:**
   The final due diligence report is saved as `outputs/startup_due_diligence_report.docx` and can be downloaded or shared.

---

## Usage

1. **Edit your startup description:**

   * Update `inputs/startup_description.txt` with your startup’s details.

2. **Run the pipeline:**

   ```bash
   python run_pipeline.py
   ```

3. **Find your results:**

   * The console will show each section’s output.
   * The full report is generated at `outputs/startup_due_diligence_report.docx`.

---

## Customization

* **Change/extend agents:**
  All agent logic and prompts are in `agents/`.
  Add new agents or modify existing ones for deeper analysis or different question sets.

* **Modify pipeline logic:**
  Change the order of analysis, questions, or add custom pre/post-processing in `run_pipeline.py`.

* **API model selection:**
  Update `llm.py` to use a different Gemini model version if needed.

---

## Agents & Their Roles

* `FounderAgent`: Simulates the founder, providing vision and context.
* `MarketAnalystAgent`: Analyzes market size, growth, and trends.
* `ProductReviewerAgent`: Evaluates product differentiation and readiness.
* `CompetitorScoutAgent`: Maps and compares key competitors.
* `TechAuditorAgent`: Audits tech stack, scalability, and feasibility.
* `RiskOfficerAgent`: Flags business, legal, and technical risks.
* `InvestmentAdvisorAgent`: Provides an investment recommendation.
* `SynthesizerAgent`: Combines all findings into a summary.
* `ReportWriterAgent`: Formats everything into a report.
* `VCPartnerAgent`: Makes a final investment decision (GO/NO-GO).

---

## Example Output

After running the pipeline, you’ll get a detailed, sectioned due diligence report—**ready for VCs, founders, or analysts**.
See `outputs/startup_due_diligence_report.docx` for the latest generated sample.


