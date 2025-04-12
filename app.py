
import streamlit as st
from transformers import pipeline
from fpdf import FPDF

# Load model using a public one
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

generator = load_model()

# Page config
st.set_page_config(page_title="Explain Like I'm 5", page_icon="🧸", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧸 Explain Like I'm 5</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask anything and I’ll explain it super simply 👶</p>", unsafe_allow_html=True)

# Input
user_input = st.text_input("🎯 Enter a topic or question:", placeholder="e.g., What is blockchain?")

with st.expander("💡 Try These Examples"):
    st.markdown("- What is AI?\n- Why is the sky blue?\n- How does Wi-Fi work?\n- What is climate change?")

# Generate explanation
def generate_eli5_response(topic):
    prompt = f"Explain this to a 5-year-old: {topic}"
    result = generator(prompt, max_new_tokens=150, do_sample=True, temperature=0.7)
    return result[0]['generated_text'].replace(prompt, "").strip()

# PDF Export
def export_to_pdf(topic, explanation):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Topic: {topic}\n\nExplanation:\n{explanation}")
    return pdf.output(dest='S').encode('latin-1')

# Run
if st.button("✨ Explain it to me!"):
    if user_input.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Explaining like you're 5..."):
            explanation = generate_eli5_response(user_input)
            st.success("🍼 Here's your explanation:")
            st.markdown(f"**{explanation}**")

            # Export to PDF
            pdf_data = export_to_pdf(user_input, explanation)
            st.download_button("📄 Download as PDF", data=pdf_data, file_name=f"ELI5-{user_input[:30]}.pdf", mime="application/pdf")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>❤️ Made with Love. By Akash Shahade</p>", unsafe_allow_html=True)
