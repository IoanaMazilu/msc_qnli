# Premise: Arun purchased 30 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased less than 50 kg of wheat at the rate of Rs.
# Golden Label: entailment

wheat_purchased_premise = 30
wheat_purchased_hypothesis = 50

# the hypothesis refers to the weight of wheat purchased, which is also mentioned in the premise
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # check if the hypothesis estimate contradicts the weight of wheat purchased in the premise
    label = "contradiction"
elif wheat_purchased_premise < wheat_purchased_hypothesis:
    # if the weight of purchased wheat in the premise is less than the hypothesis estimate, we can infer entailment
    label = "entailment"
else:
    # any other case would be neutral
    label = "neutral"

print(label)

