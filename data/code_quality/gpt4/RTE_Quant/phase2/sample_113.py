budget_premise = 1.8e9
partnerships_premise = 500
partnerships_hypothesis = 500

# the hypothesis talks about the number of partnerships with small companies, which is not detailed in the premise
# the premise only mentions the total number of partnerships, not specifically with small companies
# the hypothesis cannot be fully entailed from the premise, since we don't know the exact number of partnerships with small companies
label = "neutral"

print(label)
