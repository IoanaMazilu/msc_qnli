# Premise: less than 30% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Hypothesis: 10% people of a village in Sri Lanka died by bombardment, 20% of the remainder left the village on account of fear.
# Golden Label: neutral

death_rate_premise = 0.30
death_rate_hypothesis = 0.10
fearful_departure_rate = 0.20

# the hypothesis refers to the death and departure rates mentioned in the premise
if death_rate_hypothesis > death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif death_rate_hypothesis < death_rate_premise:
    # the death rate in the hypothesis is less than in the premise, which is consistent with the premise
    # however, it cannot be explicitly entailed from the premise, since the premise only gives a upper limit for the death rate
    label = "neutral"
else:
    # if the death rate in the hypothesis equals the one in the premise, we check the departure rate
    if fearful_departure_rate != 0.20:
        # check if the departure rate in the hypothesis contradicts the one in the premise
        label = "contradiction"
    else:
        # if both rates in the hypothesis equal the ones in the premise, we can infer entailment
        label = "entailment"

print(label)

