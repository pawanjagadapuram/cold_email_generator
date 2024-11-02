import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from email_generator import EmailGenerator
from portfolio_manager import PortfolioManager
from text_processor import clean_webpage_content

class ColdEmailApp:
    def __init__(self):
        self.email_generator = EmailGenerator()
        self.portfolio_manager = PortfolioManager()
        
    def setup_page_config(self):
        st.set_page_config(
            page_title="Cold Email Generator",
            page_icon="📧",
            layout="wide"
        )
        
    def render_interface(self):
        st.title("Cold Email Generator")
        url_input = st.text_input(
            "Enter company careers page URL:",
            value="https://www.example.com",
            help="Paste the URL of the job posting you're interested in"
        )
        return url_input, st.button("Generate Email")
        
    def process_url(self, url):
        try:
            # Load and clean webpage content
            loader = WebBaseLoader([url])
            webpage_content = clean_webpage_content(loader.load().pop().page_content)
            
            # Initialize portfolio and extract jobs
            self.portfolio_manager.load_portfolio()
            job_listings = self.email_generator.extract_jobs(webpage_content)
            
            # Generate emails for each job
            for job in job_listings:
                required_skills = job.get("skills", [])
                portfolio_links = self.portfolio_manager.query_links(required_skills)
                email_content = self.email_generator.write_mail(job, portfolio_links)
                
                # Display job role and generated email
                st.subheader(f"Email for {job.get('role', 'Position')}")
                st.code(email_content, language="markdown")
                
        except Exception as e:
            st.error(f"Error processing URL: {str(e)}")
            
    def run(self):
        self.setup_page_config()
        url, submit = self.render_interface()
        
        if submit:
            self.process_url(url)

if __name__ == "__main__":
    app = ColdEmailApp()
    app.run()