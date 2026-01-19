**Large Language Models and Law**  
**Prof. Elliott Ash**

 **Day 2 Course Worksheet**  
([link to this page](https://eash.cc/llml-w2): [eash.cc/llml-w2](http://eash.cc/llml-w2))

Make a copy of this doc (under “File… Make a Copy”) for adding your own notes, filling in exercises, and for your personal reference after the course. 

## **Exercise. You have an army of very good paralegals that are experts in your area of law. They work for 25 cents an hour and work all day and night. That is, you have legal AI. Think of an idea for what you would do, in terms of offering legal services, using such a technology. Use an LLM to help you brainstorm. Paste the conversation thread and a summary of the idea.**

|  |
| :---- |

# Day 1 Recap

* [chatgpt.com](http://chatgpt.com) (or [gemini.google.com](http://gemini.google.com) or [claude.ai](https://claude.ai/) or [grok.com](http://grok.com) )  
* Interface  
  * Attachments  
  * search the web  
  * Model flavors  
  * New Chat  
  * Context Length  
  * Share Chat  
  * Voice Mode  
* Custom Prompt  
  * *I am a law student doing coursework on X and X, with expertise in X and X.*   
  * *Answer concisely, in English or X. Legal jargon is OK.* 

# Some Law School Tasks

**Preparing for class**

* \[copy paste the case\]  
* give me the IRAC analysis of this case.  
* voice mode: You are a law professor. Conduct a Socratic examination of this case, asking one question at a time and waiting for my response before continuing.

**Quiz yourself**

* *Give me 5 multiple choice questions about this case*  
* *Give me 50 multiple choice questions about this list of court cases*  
* *Give me 50 multiple choice questions about this casebook*

**Academic research**

* *trace the origin and evolution of the word “employee”*  
* *Give me an outline for a course paper on an Originalist approach to internet regulation.*  
* *I am in a seminar course on law and technology, and my professor uses both economics and history approaches. Give me 5 ideas for my course paper.*  
* *Here is the course syllabus. Give me 5 more.*

**Public relations, e.g. social media posts**

* *Write a LinkedIn post describing this brief submitted by my law clinic.* 

# Prompting LLMs

\[slides\]

# LLMs with Knowledge Retrieval

\[slides\]

[**Perplexity**](http://perplexity.ai): [Example Search on hallucinated cases](https://www.perplexity.ai/search/recent-legal-case-hallucinatio-hvqm2r5nRu6YG_BD12s5rQ?sm=d#0)

Notebook LM (Gemini)

Deep Research (ChatGPT, Claude, Grok)

# Custom Assistants

\[slides\]

* Explore GPTS . . \+ Create   
* Create – GPT Builder  
* Configure – system prompt  
  * *Your task is to prepare an outline of a case. I will provide the text of the case and some notes I took in class. Write an outline motivated by the notes, quoting relevant excerpts, with citations. Here is the format for outlines I prefer . . .*  
* Configure – upload files  
  * *a legal assistant for new york tenants rights, with a few custom documents that i will upload*  
    * [*https://ag.ny.gov/sites/default/files/tenants\_rights.pdf*](https://ag.ny.gov/sites/default/files/tenants_rights.pdf)  
    * [*https://www.nycourts.gov/courtsnychousing/pdfs/Landlordbooklet.pdf*](https://www.nycourts.gov/courtsnychousing/pdfs/Landlordbooklet.pdf)  
  * A legal assistant for intellectual property  
    * [example textbook](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1172142)

## **Exercise. Make a custom AI assistant with an attached knowledge base. Paste a link.**

|  |
| :---- |

---

# Analytics with LLM Code Interpreter

**Tabular data:**

* *load a dataset*  
  * example dataset: [SCDB judge level data](http://scdb.wustl.edu/_brickFiles/2025_01/SCDB_2025_01_justiceCentered_LegalProvision.csv.zip)  
* *tell me about this dataset*  
* *give me summary statistics*  
* *plot histograms of the main variables*  
  * *lawtype, majVotes, minVotes*  
* *compute the average direction by issuearea by decade, and plot that*  
* *compute the average direction for each judge, rank the top 10 judges for each category.*  
* *regress splitVote on issueArea with judge fixed effects and clustering by judge*

**Text data:**

* *load a text dataset*  
  * [1000 SCOTUS opinion texts](https://www.dropbox.com/scl/fi/1lprngeghlywelye4alc6/SCOTUS-opinions-1000.zip?rlkey=pppg49tok2nwv0ujdqgwg0sy3&st=61xpj6qi&raw=1)  
  * ([full dataset here](https://www.kaggle.com/datasets/gqfiddler/scotus-opinions?resource=download))  
* *give me a list of terms associated with X*   
* *add a new column that counts these terms in the text field, after removing capitalization*  
* *plot this variable by decade*  
* *rank each judge by the usage of the term X.*   
* *do a text match to tag citations to all constitutional amendments, then tell me which amendments are most associated with decisiondirection conservative (1) or liberal (2), using an odds ratio. drop decision direction unspecified (3).*


# Agent mode

* find all of the judges in the new york supreme court in manhattan. find out bio information about them, including age, place of origin, political party / donations / activities, academic research, and philanthropic activities.