# Premise: Jagtap purchases 30 kg of wheat at the rate of 11.50 per kg and 20 kg of wheat at the rate of 14.25 per kg.
# Hypothesis: Jagtap purchases 20 kg of wheat at the rate of 11.50 per kg and 20 kg of wheat at the rate of 14.25 per kg.
# Golden Label: contradiction

# quantities from the premise
wheat_quantity1_premise = 30
wheat_rate1_premise = 11.50
wheat_quantity2_premise = 20
wheat_rate2_premise = 14.25

# quantities from the hypothesis
wheat_quantity1_hypothesis = 20
wheat_rate1_hypothesis = 11.50
wheat_quantity2_hypothesis = 20
wheat_rate2_hypothesis = 14.25

# the hypothesis makes a claim about the quantities and rates of wheat purchased, which are also mentioned in the premise
if wheat_quantity1_hypothesis != wheat_quantity1_premise or wheat_rate1_hypothesis != wheat_rate1_premise:
    # check if the quantity or rate of the first wheat purchase in the hypothesis contradict the premise
    label = "contradiction"
elif wheat_quantity2_hypothesis != wheat_quantity2_premise or wheat_rate2_hypothesis != wheat_rate2_premise:
    # check if the quantity or rate of the second wheat purchase in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

