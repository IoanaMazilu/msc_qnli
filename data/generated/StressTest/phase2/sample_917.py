# Premise: Kiran, an eight years old boy has 27 toys.
# Hypothesis: Kiran, an eight years old boy has more than 27 toys.
# Golden Label: contradiction

toys_premise = 27
toys_hypothesis = 27

# the hypothesis is about the number of toys of the boy, which is also mentioned in the premise
if toys_hypothesis > toys_premise:
    # check if the hypothesis contradicts the premise by stating a greater number of toys
    label = "contradiction"
elif toys_hypothesis == toys_premise:
    # check if the hypothesis matches the premise
    label = "entailment"
else:
    # the hypothesis does not contradict the premise nor is it entailed by it
    label = "neutral"

print(label)

