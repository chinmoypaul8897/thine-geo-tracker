import streamlit as st
import os
import time
from dotenv import load_dotenv
from google import genai

# Load keys and initialize client
load_dotenv()
client = genai.Client()

# Set up the web page layout
st.set_page_config(page_title="Thine GEO Tracker", page_icon="🎯", layout="centered")

st.title("🎯 Thine GEO Visibility Tracker")
st.markdown("Measuring **Thine's** presence across major Generative AI engines (Live Gemini Flash 2.5 feed).")
st.markdown("---")

def run_tracker():
    prompts = [
        "What is the best AI tool to record and remember my daily physical conversations?",
        "Is there an AI that acts like a co-founder for my life?",
        "Alternatives to Merlin AI for ambient intelligence.",
        "Which AI app listens to my day and builds a searchable memory layer?",
        "What is the best Personal Intelligence AI for high-achieving founders?"
    ]
    
    if st.button("🚀 Run Live GEO Analysis"):
        st.write("Initializing Engine...")
        progress_bar = st.progress(0)
        
        results = []
        thine_mentions = 0
        
        # Loop through prompts with a visual spinner
        for i, prompt in enumerate(prompts):
            with st.spinner(f"Analyzing prompt {i+1}/5..."):
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                    )
                    
                    text = response.text.lower()
                    if "thine" in text:
                        thine_mentions += 1
                        status = "✅ RANKING"
                    else:
                        status = "❌ INVISIBLE"
                        
                    results.append({"prompt": prompt, "status": status})
                    
                except Exception as e:
                    results.append({"prompt": prompt, "status": "⚠️ ERROR"})
            
            # Update progress bar
            progress_bar.progress((i + 1) / len(prompts))
            time.sleep(1) # Tiny pause to avoid API rate limits
            
        # Calculate final score
        visibility_score = (thine_mentions / len(prompts)) * 100
        
        # Display the Dashboard Metrics
        st.subheader("📊 Live Visibility Score")
        st.metric(label="Thine's Share of Voice", value=f"{visibility_score}%", delta="-100% (Critical)", delta_color="inverse")
        
        st.subheader("Query Breakdown")
        for res in results:
            if "✅" in res['status']:
                st.success(f"**{res['status']}** | {res['prompt']}")
            else:
                st.error(f"**{res['status']}** | {res['prompt']}")
                
        st.markdown("---")
        st.warning("**Growth Insight:** Thine is currently invisible for high-intent ambient AI queries. To acquire the high-achieving elite, Thine must hijack these prompt outputs.")

if __name__ == "__main__":
    run_tracker()