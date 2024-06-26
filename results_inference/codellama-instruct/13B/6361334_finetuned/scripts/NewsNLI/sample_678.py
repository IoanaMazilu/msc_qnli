minor_injuries_premise = 100
serious_injuries_hypothesis = 2

# the hypothesis mentions the number of serious injuries, which is not mentioned in the premise
# therefore, we cannot entail the hypothesis from the premise
label = "neutral"

print(label)
