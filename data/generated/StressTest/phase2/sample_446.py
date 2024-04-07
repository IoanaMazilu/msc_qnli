# Premise: Arun purchased 30 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased 70 kg of wheat at the rate of Rs.
# Golden Label: contradiction

wheat_purchased_premise = 30
wheat_purchased_hypothesis = 70

# the hypothesis talks about the amount of wheat purchased, which is also referenced in the premise
if wheat_purchased_hypothesis == wheat_purchased_premise:
    # check if the amount of wheat purchased in the hypothesis matches that in the premise
    label = "entailment"
elif wheat_purchased_hypothesis < wheat_purchased_premise:
    # check if the amount of wheat purchased in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the amount of wheat in the hypothesis is more than that in the premise, therefore we can't entail or contradict
    label = "neutral"

print(label)

