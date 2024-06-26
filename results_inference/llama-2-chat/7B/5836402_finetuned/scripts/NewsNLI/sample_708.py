victims_premise = 1000
victims_hypothesis = 1000
deaths_hypothesis = 2

# the hypothesis mentions the number of victims and the deaths, which are also referenced in the premise
# however, the hypothesis does not specify the location of the secret detention centers, which is a crucial detail in the premise
# hence, we cannot infer entailment or contradiction based on the given information
label = "neutral"

print(label)
