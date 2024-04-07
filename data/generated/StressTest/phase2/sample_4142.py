# Premise: Prabhu purchased 30 kg of rice at the rate of 17.50 per kg and another 30 kg rice at a certain rate.
# Hypothesis: Prabhu purchased more than 30 kg of rice at the rate of 17.50 per kg and another 30 kg rice at a certain rate.
# Golden Label: contradiction

rice_kg_1_premise = 30
rice_kg_1_hypothesis = 30
rate_1_premise = 17.50
rate_1_hypothesis = 17.50
rice_kg_2_premise = 30
rice_kg_2_hypothesis = 30

# the hypothesis refers to the amount of rice and the rate that Prabhu purchased in the premise
if rice_kg_1_hypothesis <= rice_kg_1_premise:
    # check if the amount of rice purchased at a certain rate in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif rate_1_hypothesis != rate_1_premise:
    # check if the rate at which rice was purchased in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
elif rice_kg_2_hypothesis != rice_kg_2_premise:
    # check if the amount of rice purchased at a certain rate in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

