# The premise and hypothesis refer to the same situation, but with different percentages

# The hypothesis mentions a higher percentage than in the premise (40% vs 50%)
if percent_premise > percent_hypothesis:
    # If the percentage in the hypothesis is greater than the percentage in the premise, we can infer entailment
    label = "entailment"
elif percent_premise == percent_hypothesis:
    # If the percentage in the hypothesis is equal to the percentage in the premise, we can infer neutrality
    label = "neutral"
else:
    # If the percentage in the hypothesis is less than the percentage in the premise, we can infer contradiction
    label = "contradiction"

print(label)
