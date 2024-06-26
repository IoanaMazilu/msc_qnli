non_hybrid_tajimas_premise = 65
multiplier_hybrid_tajimas = 3
non_hybrid_tajimas_hypothesis = 35

# The hypothesis and premise are talking about the relationship between the number of non hybrid Tajima's and the number of hybrid Tajima's.
if non_hybrid_tajimas_hypothesis > non_hybrid_tajimas_premise:
    # If the number in the hypothesis is greater than the number in the premise, then it contradicts the premise.
    label = "contradiction"
elif non_hybrid_tajimas_hypothesis < non_hybrid_tajimas_premise:
    # If the number in the hypothesis is less than the number in the premise, then it doesn't contradict it but it also cannot be explicitly entailed from the premise.
    label = "neutral"
else:
    # If both numbers match, then the hypothesis can be fully and explicitly entailed from the premise.
    label = "entailment"

print(label)
