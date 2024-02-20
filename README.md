## **Practical Natural Language Generation Evaluation**  
 _Evaluate Chatbots for Your Business_  

### **Overview**
This repository explores the latest NLG evaluation techniques in the context of everyday businesses.

The majority of businesses are not creating foundational models from scratch. Instead, they are adapting foundational LLM models such as GPT4-turbo or Llamma to develop specific solutions, utilizing prompt engineering, RAG, or fine-tuning.

Common evaulation frameworks such as MMLU, L-eval, and HellaSwag are great for foundational model analysis, but do not cover evaluation of adapted mode or chatbot outputs after Prompting, RAG or Fine-Tuning.  

The goals of these labs is to provide a framework to enable you to answer the question: **Is my model safe, effective, and accurate enough to deploy to Production?**

### **Getting Started**  
This repository contains [Demo Notebooks](./demo_notebooks/) and accompanying [source code](./src/) for vairous evaluation scenarios.  
  
- **Demo Notebooks:** Step-by-Step interactive walkthroughs of various eval techniques
  - 0_setup: _Environment and development setup_
  - 1_gpt_evaluation: _Evaluate Fluency, Coherence, & Relevance using GPT4_
  - 2_gpt_eval_benchmark: _Compare GPT graded Coherence to human analysis. Test new prompts for evaluation_
  - 3_rag_evaluation: _Evaluate the quality of Context against both Question and Answer using GPT based Groundedness and embedding cosine similarity_
  - 4_RAGAS: _Evaluate RAG based NLG using the [RAGAS](https://github.com/explodinggradients/ragas) framework_
  - 5_hallucination_detection: _Explore methods for inline hallucination detection_
- **Source Code:** Reference source code to go along with each notebook demo.


