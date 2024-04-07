# Premise: Jaydeep purchased less than 75 kg of rice at the rate of 16.50 per kg and 35 kg of rice at the rate of 24.50 per kg.
# Hypothesis: Jaydeep purchased 25 kg of rice at the rate of 16.50 per kg and 35 kg of rice at the rate of 24.50 per kg.
# Golden Label: neutral

rice_weight_premise = 75
rice_weight_hypothesis = 25
rice_rate1 = 16.50
rice_rate2 = 24.50
rice_weight2_premise = rice_weight2_hypothesis = 35

# the hypothesis refers to the quantity and rate of rice purchased, also mentioned in the premise
if rice_weight_premise <= rice_weight_hypothesis:
    # check if the quantity of rice in the hypothesis contradicts the estimate of less than 'rice_weight_premise'
    label = "contradiction"
elif rice_rate1 != rice_rate1 or rice_rate2 != rice_rate2 or rice_weight2_premise != rice_weight2_hypothesis:
    # check if the rates or the second quantity of rice in the hypothesis contradict the rates or the second quantity of rice reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and rates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

