people_premise = 200
people_hypothesis = 200

# the hypothesis mentions the exact same number of people as the premise
if people_hypothesis!= people_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
