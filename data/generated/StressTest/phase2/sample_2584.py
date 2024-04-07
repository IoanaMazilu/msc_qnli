# Premise: Tom purchased more than 7 kg of apples at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Hypothesis: Tom purchased 8 kg of apples at the rate of 70 per kg and 9 kg of mangoes at the rate of 55 per kg.
# Golden Label: neutral

apples_kg_premise = 7
apples_kg_hypothesis = 8
apples_rate_premise = 70
apples_rate_hypothesis = 70
mangoes_kg_premise = 9
mangoes_kg_hypothesis = 9
mangoes_rate_premise = 55
mangoes_rate_hypothesis = 55

# the hypothesis refers to the number of kg of apples and mangoes purchased by Tom, as well as their rate per kg
if apples_kg_hypothesis <= apples_kg_premise or apples_rate_hypothesis != apples_rate_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'apples_kg_premise' kg of apples
    # or if the rate per kg of apples in the hypothesis contradicts the rate in the premise
    label = "contradiction"
elif mangoes_kg_hypothesis != mangoes_kg_premise or mangoes_rate_hypothesis != mangoes_rate_premise:
    # check if the number of kg of mangoes in the hypothesis contradicts the number of kg in the premise
    # or if the rate per kg of mangoes in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of apples
    # any number of kg greater than 'apples_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

