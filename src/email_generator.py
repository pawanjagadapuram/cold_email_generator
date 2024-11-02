import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class EmailGenerator:
    def __init__(self):
        self._initialize_llm()
        self._setup_prompts()
        
    def _initialize_llm(self):
        """Initialize the LLM with appropriate configuration"""
        self.llm = ChatGroq(
            model_name="llama-3.1-70b-versatile",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        
    def _setup_prompts(self):
        """Set up prompt templates for job extraction and email generation"""
        self.job_extraction_prompt = PromptTemplate.from_template("""
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """)
            
        self.email_generation_prompt = PromptTemplate.from_template("""
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Pawan, a software developer with over 4 years of experience in Software Development, currently pursuing an MS in Computer Science at the University of Florida. 
            Your background includes developing efficient, scalable, and user-centered applications across various domains, with a focus on optimizing performance, enhancing user experience, and integrating complex functionalities seamlessly. 
            Your job is to write a cold email to the client regarding the job mentioned above, showcasing how your technical skills, experience, and ongoing advanced studies make you well-equipped to fulfill their needs and add value to their team. 
            Also, include relevant portfolio links as examples of past projects that highlight your skills: {link_list}
            Remember you are Pawan, a software developer with advanced training and practical experience.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """)
    
    def extract_jobs(self, cleaned_text):
        """Extract job listings from cleaned webpage text"""
        chain = self.job_extraction_prompt | self.llm
        response = chain.invoke(input={"page_data": cleaned_text})
        
        try:
            parsed_response = JsonOutputParser().parse(response.content)
            return parsed_response if isinstance(parsed_response, list) else [parsed_response]
        except OutputParserException:
            raise OutputParserException("Unable to parse jobs due to context length or format.")
            
    def write_mail(self, job, links):
        """Generate a cold email based on job description and portfolio links"""
        chain = self.email_generation_prompt | self.llm
        response = chain.invoke({
            "job_description": str(job),
            "link_list": links
        })
        return response.content