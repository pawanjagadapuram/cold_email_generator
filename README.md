# Cold Email Generator

An AI-powered tool that automatically generates personalized cold emails for job applications by analyzing job postings and matching them with your portfolio.

## Features

- 🔍 Automatically extracts job requirements from career pages
- 📝 Generates personalized cold emails based on job descriptions
- 🔗 Intelligently matches your portfolio projects with job requirements
- 💼 Maintains a vector database of your portfolio for efficient matching
- 🎯 Utilizes "llama-3.1-70b-versatile" - LLM for accurate job parsing and email generation

## Prerequisites

- Python 3.10 or lower
- Groq API key
- Your portfolio data in CSV format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pawanjagadapuram/cold_email_generator.git
cd cold_email_generator
```

2. Install dependencies:
```bash
python3.10 -m venv env - # Create a python virtual environment
env\Scripts\activate - # Activate virtual environment
pip install -r requirements.txt - # Install requirements
```

3. Set up environment variables:
```bash
cp .env
```
Edit `.env` and add your Groq API key.

4. Prepare your portfolio:
- Place your portfolio data in `resources/portfolio.csv`
- Format should include columns: `Techstack` and `Links`

## Usage

1. Start the application:
```bash
streamlit run src/app.py
```

2. Enter the URL of the job posting/careers page you're interested in

3. Click "Generate Email" to create personalized cold emails based on the job requirements
