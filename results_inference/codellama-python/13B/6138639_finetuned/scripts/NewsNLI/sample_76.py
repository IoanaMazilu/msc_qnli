favor_premise = 0.52
favor_hypothesis = 0.52
oppose_premise = 0.46

# the hypothesis mentions the percentage of people favoring the war in Afghanistan, which is also referenced in the premise
# however, the hypothesis does not mention the percentage of people opposing the war, which is also referenced in the premise
# thus, we cannot infer entailment or contradiction
label = "neutral"

print(label)
