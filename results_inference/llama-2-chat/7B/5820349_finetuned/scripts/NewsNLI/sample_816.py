oppose_terrorism_premise = 0.62
oppose_raids_hypothesis = 0.63

# the hypothesis mentions the percentage of people who disapprove of the raid, which is also referenced in the premise
# however, the hypothesis does not mention anything about the U.S.-led efforts to fight terrorism, which is explicitly mentioned in the premise
# thus, we cannot infer entailment or contradiction based on the given information
label = "neutral"

print(label)
