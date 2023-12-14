## **Practical LLM Evaluation**  
 _Evaluate LLMs for Your Business_  

### **Overview**
This repository explores the latest LLM evaluation techniques in the context of everyday businesses.

The majority of businesses are not creating foundational models from scratch. Instead, they are adapting foundational LLM models such as GPT4-turbo or Llamma to develop specific solutions, utilizing prompt engineering, RAG, or fine-tuning.

Common evaulation benchmarks such as MMLU, L-eval, and HellaSwag are great for foundational model analysis, but miss the mark when evaluating if an adapted model is ready for production for my business.  

The goals of these labs is to provide a framework to enable you to answer the question: _Is my model safe, effective, and accurate enough to deploy to Production?_


### **Getting Started**  
This repository contains [Demo Notebooks](./demo_notebooks/) and accompanying [source code](./src/) for vairous evaluation scenarios. After completing [0_setup.ipynb](./demo_notebooks/0_setup.ipynb) demo notebooks can be run in any order.
- **Demo Notebooks:** Step-by-Step interactive walkthroughs of various eval techniques
  - 0_setup: _Environment and development setup_
  - 1_gpt_evaluation: _Evaluate Fluency, Coherence, & Relevance using GPT4_
  - 2_gpt_eval_benchmark: _Compare GPT graded Coherence to human analysis. Utilize new prompting strategies for evaluation_
- **Source Code:** Reference code to go along with each notebook demo.


