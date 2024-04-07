# Premise: 121, 144, 169, 196, 225, 256, 288, 324, 361.
# Hypothesis: less than 121, 144, 169, 196, 225, 256, 288, 324, 361.
# Golden Label: contradiction

premise_numbers = [121, 144, 169, 196, 225, 256, 288, 324, 361]
hypothesis_numbers = [121, 144, 169, 196, 225, 256, 288, 324, 361]

# the hypothesis states that all numbers are less than the given numbers in the premise
for premise, hypothesis in zip(premise_numbers, hypothesis_numbers):
    if hypothesis >= premise:
        # check if any number in the hypothesis contradicts the statement of being less than the corresponding number in the premise
        label = "contradiction"
        break
else:
    # if no hypothesis number contradicts the premise, then it's consistent with the premise
    # but due to the vague "less than" in the hypothesis, we cannot infer entailment
    label = "neutral"

print(label)

