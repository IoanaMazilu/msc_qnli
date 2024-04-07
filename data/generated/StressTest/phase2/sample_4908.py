# Premise: Jagtap purchases 30 kg of wheat at the rate of 11.50 per kg and 20 kg of wheat at the rate of 14.25 per kg.
# Hypothesis: Jagtap purchases more than 20 kg of wheat at the rate of 11.50 per kg and 20 kg of wheat at the rate of 14.25 per kg.
# Golden Label: entailment

wheat_kg_premise = 30
wheat_kg_hypothesis = 20
wheat_rate_premise = 11.50
wheat_rate_hypothesis = 11.50
wheat_kg_premise_other = 20
wheat_kg_hypothesis_other = 20
wheat_rate_premise_other = 14.25
wheat_rate_hypothesis_other = 14.25

# the hypothesis refers to the amount and rate of wheat purchased mentioned in the premise
if wheat_kg_premise <= wheat_kg_hypothesis and wheat_rate_premise == wheat_rate_hypothesis:
    # check if the weight of wheat purchased in the hypothesis contradicts the weight of wheat purchased in the premise
    label = "contradiction"
elif wheat_kg_premise_other != wheat_kg_hypothesis_other and wheat_rate_premise_other == wheat_rate_hypothesis_other:
    # check if the weight of other wheat purchased in the hypothesis contradicts the weight of other wheat purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

