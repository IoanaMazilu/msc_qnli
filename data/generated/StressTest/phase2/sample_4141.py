# Premise: Prabhu purchased more than 10 kg of rice at the rate of 17.50 per kg and another 30 kg rice at a certain rate.
# Hypothesis: Prabhu purchased 30 kg of rice at the rate of 17.50 per kg and another 30 kg rice at a certain rate.
# Golden Label: neutral

rice_kg_premise = 10
rice_kg_hypothesis = 30
rate_premise = 17.50
rate_hypothesis = 17.50

# the hypothesis refers to the amount of rice purchased and the rate mentioned in the premise
if rice_kg_hypothesis <= rice_kg_premise:
    # check if the amount of rice in the hypothesis contradicts the amount of rice in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of rice
    # any amount of rice greater than 'rice_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

