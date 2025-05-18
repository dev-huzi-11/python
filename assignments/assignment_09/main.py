import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fpdf import FPDF
import unicodedata

# Configure the Streamlit app page settings (title and icon)
st.set_page_config(
    page_title="StartupCue - Marketing Strategy Generator",
    page_icon="🚀"
)

# Load environment variables from a .env file (such as GEMINI_API_KEY)
load_dotenv()

# Configure Gemini AI API with the API key from environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class MarketingStrategyGenerator:
    """
    A class to handle generating marketing strategies
    using Google's Gemini generative AI model.
    """

    def __init__(self, model_name: str = "gemini-2.0-flash"):
        # Initialize the Gemini generative model with the given model name
        self.model = genai.GenerativeModel(model_name=model_name)

    def generate_prompt(self, description: str, target_audience: str, goal: str) -> str:
        """
        Construct a prompt string with the product description,
        target audience, and marketing goal to send to the AI.
        """
        return f"""
        Marketing strategy from an expert marketing strategist.
        Product description: {description}
        Target audience: {target_audience}
        Marketing goal: {goal}
        Suggest a detailed marketing strategy and best platforms to run ad campaigns.
        """

    def get_strategy(self, description: str, target_audience: str, goal: str) -> str:
        """
        Use the Gemini AI model to generate a marketing strategy text
        based on the provided inputs.
        """
        prompt = self.generate_prompt(description, target_audience, goal)
        response = self.model.generate_content(prompt)
        return response.text


class AppUI:
    """
    A class to manage the Streamlit user interface and PDF generation.
    """

    def __init__(self):
        # Initialize the marketing strategy generator instance
        self.generator = MarketingStrategyGenerator()

    def clean_text(self, text: str) -> str:
        """
        Normalize text to ASCII by removing special Unicode characters,
        which ensures compatibility with PDF generation.
        """
        return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

    def create_pdf(self, content: str) -> bytes:
        """
        Generate a PDF from the given content string.
        Returns the PDF data as bytes encoded with 'latin1',
        suitable for downloading.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        cleaned = self.clean_text(content)
        pdf.multi_cell(0, 10, cleaned)
        # Output PDF as string, then encode to bytes for Streamlit download
        return pdf.output(dest='S').encode('latin1')

    def run_app(self) -> None:
        """
        Main method to run the Streamlit app interface,
        handle user inputs, generate strategy, display it,
        and provide a PDF download option.
        """
        st.title("StartupCue 🚀")
        st.markdown("Enter your product details and I'll give you a guaranteed return strategy!")

        # Input fields for product description, target audience, and goal
        description = st.text_area("Enter product description")
        target_audience = st.text_input("Enter your target audience")
        goal = st.selectbox("Marketing goal", ["Brand Awareness", "Engagement", "Sales"])

        if st.button("Generate Strategy"):
            # Validate required fields are filled
            if description and target_audience:
                with st.spinner("Analyzing and generating the best marketing strategy..."):
                    # Get strategy from AI and create PDF
                    strategy = self.generator.get_strategy(description, target_audience, goal)
                    pdf = self.create_pdf(strategy)
                st.success("Strategy generated successfully!")

                # Display strategy text in app
                st.subheader("📈 Marketing Strategy")
                st.write(strategy)

                # Provide PDF download button with correct data (bytes)
                st.download_button(
                    label="📄 Download Strategy as PDF",
                    data=pdf,  
                    file_name="marketing_strategy.pdf",
                    mime="application/pdf"
                )
            else:
                # Warn if required inputs missing
                st.warning("Please fill all the fields")


if __name__ == "__main__":
    app = AppUI()
    app.run_app()
