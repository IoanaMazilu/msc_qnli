people_killed_premise = 3
people_killed_hypothesis = 32

# the hypothesis mentions the number of people killed, which is also referenced in the premise
# however, the hypothesis refers to a different location (Madalla) than the one mentioned in the premise (Damaturu)
# thus, we cannot infer entailment or contradiction based on the information provided
label = "neutral"

print(label)
