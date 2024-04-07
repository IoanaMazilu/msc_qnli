# Premise: Arun purchased 30 kg of wheat at the rate of Rs.
# Hypothesis: Arun purchased 80 kg of wheat at the rate of Rs.
# Golden Label: contradiction

wheat_purchase_premise = 30
wheat_purchase_hypothesis = 80

# the hypothesis refers to the amount of wheat purchased, also mentioned in the premise
if wheat_purchase_hypothesis != wheat_purchase_premise:
    # check if the amount of wheat purchased in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

