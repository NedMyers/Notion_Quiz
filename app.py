import os
from flask import Flask
from groq import Groq
from pypdf import PdfReader

app = Flask(__name__)
def pdf_reader(pdf_path):
    reader = PdfReader(pdf_path)
    pdf_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"
    return(pdf_text)



@app.route('/')
def run_my_script():

    # Initialize the client with your key
    client = Groq(api_key="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")
    
    #  Define your question
    question = "Please can you create a 20 question multiple choice quiz based on this lecture. Don't give the answers until the end. Do not put them in a grid format"
    
    #  Send the question and the PDF text to Groq
    prompt = f"""
    You are a helpful assistant. Use the following document text to answer the question.
    
    Document Text:
    {pdf_reader("Lecture_PageRank.pdf")}
    
    Question: {question}
    """
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="openai/gpt-oss-120b", # Or another current model
    )
    
    return chat_completion.choices[0].message.content

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
