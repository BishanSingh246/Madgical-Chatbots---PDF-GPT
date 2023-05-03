"""
This module provides functions for working with PDF files and URLs. It uses the urllib.request library
to download files from URLs, and the fitz library to extract text from PDF files. And GPT3 modules to generate
text completions.
"""
import fitz
import re
import numpy as np
import tensorflow_hub as hub
import openai
import gradio as gr
import os
from sklearn.neighbors import NearestNeighbors
from pdfQuestions import dataFromPDF

def preprocess(text):
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text


def pdf_to_text(path, start_page=1, end_page=None):
    doc = fitz.open(path)
    total_pages = doc.page_count

    if end_page is None:
        end_page = total_pages

    text_list = []

    for i in range(start_page-1, end_page):
        text = doc.load_page(i).get_text("text")
        text = preprocess(text)
        text_list.append(text)

    doc.close()
    return text_list


def text_to_chunks(texts, word_length=150, start_page=1):
    text_toks = [t.split(' ') for t in texts]
    page_nums = []
    chunks = []
    
    for idx, words in enumerate(text_toks):
        for i in range(0, len(words), word_length):
            chunk = words[i:i+word_length]
            if (i+word_length) > len(words) and (len(chunk) < word_length) and (
                len(text_toks) != (idx+1)):
                text_toks[idx+1] = chunk + text_toks[idx+1]
                continue
            chunk = ' '.join(chunk).strip()
            chunk = f'[{idx+start_page}]' + ' ' + '"' + chunk + '"'
            chunks.append(chunk)
    return chunks


class SemanticSearch:
    
    def __init__(self):
        self.use = hub.load('https://tfhub.dev/google/universal-sentence-encoder/4')
        self.fitted = False
    
    
    def fit(self, data, batch=1000, n_neighbors=5):
        self.data = data
        self.embeddings = self.get_text_embedding(data, batch=batch)
        n_neighbors = min(n_neighbors, len(self.embeddings))
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)
        self.nn.fit(self.embeddings)
        self.fitted = True
    
    
    def __call__(self, text, return_data=True):
        inp_emb = self.use([text])
        neighbors = self.nn.kneighbors(inp_emb, return_distance=False)[0]
        
        if return_data:
            return [self.data[i] for i in neighbors]
        else:
            return neighbors
    
    
    def get_text_embedding(self, texts, batch=1000):
        embeddings = []
        for i in range(0, len(texts), batch):
            text_batch = texts[i:(i+batch)]
            emb_batch = self.use(text_batch)
            embeddings.append(emb_batch)
        embeddings = np.vstack(embeddings)
        return embeddings



def load_recommender(path, start_page=1):
    global recommender
    texts = pdf_to_text(path, start_page=start_page)
    chunks = text_to_chunks(texts, start_page=start_page)
    recommender.fit(chunks)
    return 'Corpus Loaded.'

def generate_text(openAI_key,prompt, engine="text-davinci-003"):
    openai.api_key = openAI_key
    completions = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message

def generate_answer(question,openAI_key):
    topn_chunks = recommender(question)
    prompt = ""
    prompt += 'search results:\n\n'
    for c in topn_chunks:
        prompt += c + '\n\n'
        
    prompt += "Instructions: Compose a comprehensive reply to the query using the search results given. "\
              "Cite each reference using [ Page Number] notation (every result has this number at the beginning). "\
              "Citation should be done at the end of each sentence. If the search results mention multiple subjects "\
              "with the same name, create separate answers for each. Only include information found in the results and "\
              "don't add any additional information. Make sure the answer is correct and don't output false content. "\
              "If the text does not relate to the query, simply state 'Text Not Found in PDF'. Ignore outlier "\
              "search results which has nothing to do with the question. Only answer what is asked. The "\
              "answer should be short and concise. Answer step-by-step. \n\nQuery: {question}\nAnswer: "
    
    prompt += f"Query: {question}\nAnswer:"
    answer = generate_text(openAI_key, prompt,"text-davinci-003")
    return answer


def question_answer(file,question,openAI_key):
    
    if openAI_key.strip()=='':
        return '[ERROR]: Please enter you Open AI Key. Get your key here : https://platform.openai.com/account/api-keys'


    file_paths = ["./Smart Protect Goal Brochure.pdf", "./Future Wealth Gain Brochure.pdf"]
    for path in file_paths:
        if file in path:
            load_recommender(path)
            print(path)

    if question.strip() == '':
        return '[ERROR]: Question field is empty'

    return generate_answer(question,openAI_key)

def allQuestion(file):

    questionOptions1 = ["What are the various options under Life Cover Variant?","What are the Add-on covers options under Variant description Life Cover?","What is the total claim covered under Minor and Major CI?","What is Waiver of Premium Benefit on CI?","What is Annualized Premium under Life Cover Variant?","Does the ROP include GST?","Under what condition is Add-on Covers applicable?","What is the duration period of premiums for CIB & WOPBI?","What is the maximum maturity age with ROP under the variant?","What is the maximum maturity age with Whole Life under the variant?"]

    questionOptions2 = ["What is Future Wealth Gain plan?","If the customer has done a partial withdrawls, is he eligible for the Loyalty Additions/Fund Boosters?","What are the steps to select the plan?","What are the maturity benefits available in the wealth plus variant of this plan?","How can one revive a discontinued policy?",'What are the tax benefit options available under this policy?','What are the features under "Wealth Plus" & "Wealth Plus Care" Variant?',"Can I switch between the funds?"]

    if file  == None:
        return '[ERROR]: Provide select atleast one option.'
    if file  == "Smart Protect Goal Brochure":
        question = questionOptions1
    if file == "Future Wealth Gain Brochure":
        question = questionOptions2
    
    return gr.Dropdown.update(choices=question)


recommender = SemanticSearch()

title = 'Madgical Chatbots - PDF GPT'
description = """ This chatbot will generate answer from PDF file :"""
options = ['Smart Protect Goal Brochure', 'Future Wealth Gain Brochure']

newOption = None

with gr.Blocks() as demo:

    gr.Markdown(f'<center><h1>{title}</h1></center>')
    gr.Markdown(f'<center><h4>{description}</h4></center>')
    

    with gr.Row():
        
        with gr.Group():
            openAI_key=gr.Textbox(label='Enter your OpenAI API key here')
            file = gr.Dropdown(options, label="Select PDF file from below options")
            btn2 = gr.Button(value='Submit')
            question = gr.Dropdown(newOption,label="Select questions from below options")
            btn = gr.Button(value='Submit')
            btn.style(full_width=True)
            btn2.style(full_width=True)

        with gr.Group():
            answer = gr.Textbox(label='Medgical Chatbot Answer :')
        with gr.Group():
            pdfData = gr.Textbox(label='Answer from PDF :')

        btn.click(question_answer, inputs=[file, question,openAI_key], outputs=[answer])
        btn.click(dataFromPDF, inputs=[question], outputs=[pdfData])
        btn2.click(allQuestion, inputs=[file], outputs=[question])
        
if __name__ == "__main__":
    demo.launch() 