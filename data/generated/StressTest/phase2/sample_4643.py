# Premise: Peter purchased 30 kg of rice at the rate of $11.50 per kg and 20 kg of rice at the rate of 14.25 per kg.
# Hypothesis: Peter purchased 20 kg of rice at the rate of $11.50 per kg and 20 kg of rice at the rate of 14.25 per kg.
# Golden Label: contradiction

rice1_quantity_premise = 30
rice1_rate_premise = 11.50
rice2_quantity_premise = 20
rice2_rate_premise = 14.25

rice1_quantity_hypothesis = 20
rice1_rate_hypothesis = 11.50
rice2_quantity_hypothesis = 20
rice2_rate_hypothesis = 14.25

# the hypothesis refers to the amount and price of rice Peter purchased, mentioned in the premise
if rice1_quantity_hypothesis != rice1_quantity_premise or rice1_rate_hypothesis != rice1_rate_premise:
    # check if the amount or price of rice1 in the hypothesis contradicts the amount or price of rice1 in the premise
    label = "contradiction"
elif rice2_quantity_hypothesis != rice2_quantity_premise or rice2_rate_hypothesis != rice2_rate_premise:
    # check if the amount or price of rice2 in the hypothesis contradicts the amount or price of rice2 in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

