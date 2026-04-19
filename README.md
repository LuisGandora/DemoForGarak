# DemoForGarak
4/20 Demo for Garak

# Documentation for Garak for reference
Github Doc: https://github.com/NVIDIA/garak

# Instructions
Follow these instructions to ensure this demo will work

1. Create a venv named garakStuff with the command: "python -m venv garakStuff" (reactivation: "garakStuff/Scripts/Activate" deactivate: "deactivate")


2. Install dependencies in active venv (without python -m depending on interpreter type if its not the venv)

--python -m pip install dotenv 
--python -m pip install -U garak

3. Create a .env file that contains your GROQ_API_KEY (Can be any key you want), To get one you can make one via: https://groq.com/

Ex. export GROQ_API_KEY = "sk key"

4. Run program garakdemo.py. 'test' runs the test program that just repeats the prompts inputted. 'groq' creates a groqChat as a generator to then run agains the probes

# How this works?

The primary goal of this custom probe is to check if a model will say brainrot slang even if prompted not to

First the customProbe.py acts as a probe that contains a class customProbe that has a list of prompts to ask and a primary_detector pointing to the brainrot.py. This class can then use the .probe function that accepts a generator and run tests against that

The brainrot.py acts as a detector that contains a class called KeywordDetector that checks attempts from the probe and checks if there are any brainrot slang words in the context. The checks are returned by customProbe.probe(generator) as a list then each attempt is passed through the KeywordDetector by using a in-built function called detect(). If the score returned is greater than 0, then the AI model failed that test.

The primary AI tested against this due to time constraints is Groq specifically model: llama-3.3-70b-versatile



