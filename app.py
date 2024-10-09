import streamlit as st
from transformers import pipeline
import tensorflow as tf

# Load the pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def main():
    st.title("Text Summarizer App")

    # Create a text area for the user to input the text to be summarized
    input_text = st.text_area("Enter the text you want to summarize:")

    # Create a sidebar with sliders to allow the user to customize the summary length
    st.sidebar.title("Summary Length Settings")
    min_length = st.sidebar.slider("Minimum Summary Length", 10, 200, 50)
    max_length = st.sidebar.slider("Maximum Summary Length", 50, 500, 100)

    # Create a button to trigger the summary generation process
    if st.button("Generate Summary"):
        # Check if the user has entered any text
        if input_text:
            # Generate the summary using the loaded summarizer model and the specified parameters
            summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)

            # Display the generated summary to the user
            st.subheader("Generated Summary:")
            st.write(summary[0]["summary_text"])
        else:
            # Display a warning message if the user hasn't entered any text
            st.warning("Please enter some text to summarize.")

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
