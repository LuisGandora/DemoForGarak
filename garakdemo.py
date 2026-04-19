#First activate the venv (or make one yourself with garak installed)
#Then run this script

#If you are confused use --list_generators, --list_probes, list_detectors

#For testing
from dotenv import load_dotenv
load_dotenv()

#Generators to get
import garak.generators.test #Default Test
import garak.generators.groq #For custom check
from customProbe import customProbe

#For detector testing
from brainrot import KeywordDetector
detector = KeywordDetector()

#To initialize a report file to avoid errors
from garak import _config
import sys
class DummyReport:
    def write(self, data): pass
    def flush(self): pass

_config.transient.reportfile = DummyReport()


def main():
    #mimics the --model_type and  --model_name flags
    generator = None
    print("PICK Your options: \n'Test'->generators.test\n'groq'->llama-3.3-70b-versatile")
    op = input()
    if(op == "Test"):
        generator = garak.generators.test.Repeat()
    elif(op == "groq"):
        model_name = "llama-3.3-70b-versatile"
        generator = garak.generators.groq.GroqChat(model_name)
    else:
        print("No model picked")
        return
    #intialize probe for model of type
    probe = customProbe()
    attempts = probe.probe(generator)
    print("---INPUT---")
    #Get each attempt obtained
    for attempt in attempts:
        print(f"Prompt: {attempt.prompt}")
        print(f"AI Response: {attempt.outputs}")
        print("-" * 20)
    print("---OUTPUT---")
    for attempt in attempts:
        scores = detector.detect(attempt)
        if any(score > 0 for score in scores):
            print(f"BRAINROT DETECTED in response: {attempt.outputs}")
        else:
            print("Response is clean.")

if __name__ == "__main__":
    main()