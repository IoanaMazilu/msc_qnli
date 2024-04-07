# Premise: Arun purchased 30 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased 20 kg of wheat at the rate of Rs.
# Golden Label: contradiction

wheat_purchased_premise = 30
wheat_purchased_hypothesis = 20

# the hypothesis talks about the quantity of wheat purchased, referenced also in the premise
if wheat_purchased_premise != wheat_purchased_hypothesis:
    # check if the quantity of wheat purchased in the hypothesis contradicts the quantity mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

