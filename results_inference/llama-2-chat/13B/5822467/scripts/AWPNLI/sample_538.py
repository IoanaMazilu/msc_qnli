candy_premise = 26.0
eaten_premise = 17.0
left_hypothesis = 9.0

# compute the amount of candy left after eating
left_premise = candy_premise - eaten_premise

if left_hypothesis > left_premise:
    # the hypothesis implies that there is more candy left than the premise states
    label = "contradiction"
elif left_hypothesis < left_premise:
    # the hypothesis implies that there is less candy left than the premise states
    label = "entailment"
else:
    # the hypothesis and premise have the same value for the amount of candy left
    label = "neutral"

print(label)
