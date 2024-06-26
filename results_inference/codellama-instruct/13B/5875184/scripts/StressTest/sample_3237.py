premise = "If 20% of all the students at Morse have cars, how many students are in the three lower grades?"
hypothesis = "If less than 50% of all the students at Morse have cars, how many students are in the three lower grades?"

# extract the numerical entities from the premise and hypothesis
premise_percentage = 20
hypothesis_percentage = 50

# perform the comparison between the premise and hypothesis
if premise_percentage <= hypothesis_percentage:
    label = "entailment"
else:
    label = "contradiction"

print(label)
