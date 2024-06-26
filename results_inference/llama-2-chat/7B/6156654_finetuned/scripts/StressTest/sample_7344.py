# The premise and hypothesis mention the same event, but with different percentages of price slump
# We can compare the percentage of price slump in both the premise and hypothesis

percentage_slump_premise = 28
percentage_slump_hypothesis = 68

if percentage_slump_premise >= percentage_slump_hypothesis:
    # If the percentage of price slump in the premise is greater than or equal to the percentage of price slump in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # If the percentage of price slump in the premise is less than the percentage of price slump in the hypothesis, we can infer contradiction
    label = "contradiction"

print(label)
