# Premise: Prabhu purchased 30 kg of rice at the rate of 17.50 per kg and another 30 kg rice at a certain rate.
# Hypothesis: Prabhu purchased more than 10 kg of rice at the rate of 17.50 per kg and another 30 kg rice at a certain rate.
# Golden Label: entailment

rice_quantity1_premise = 30
rice_quantity1_hypothesis = 10
rice_rate1_premise = 17.50
rice_rate1_hypothesis = 17.50
rice_quantity2_premise = 30
rice_quantity2_hypothesis = 30

# the hypothesis refers to the quantities and rates of purchased rice mentioned in the premise
if rice_quantity1_hypothesis > rice_quantity1_premise or rice_rate1_hypothesis != rice_rate1_premise:
    # check if the hypothesis values contradict the quantities and rates of purchased rice in the premise
    label = "contradiction"
elif rice_quantity2_hypothesis != rice_quantity2_premise:
    # check if the quantity of the second batch of rice in the hypothesis contradicts the quantity reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

