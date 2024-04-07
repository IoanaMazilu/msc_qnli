# Premise: less than 50% of all fishermen in Piscataquis County are also hunters while only 20% of all hunters are fishermen.
# Hypothesis: 30% of all fishermen in Piscataquis County are also hunters while only 20% of all hunters are fishermen.
# Golden Label: neutral

fishermen_hunters_premise = 50
fishermen_hunters_hypothesis = 30
hunters_fishermen_premise = 20
hunters_fishermen_hypothesis = 20

# the hypothesis refers to the percentage of fishermen who are also hunters and the percentage of hunters who are also fishermen
if fishermen_hunters_hypothesis > fishermen_hunters_premise:
    # check if the percentage of fishermen who are also hunters in the hypothesis contradicts the premise
    label = "contradiction"
elif hunters_fishermen_hypothesis != hunters_fishermen_premise:
    # check if the percentage of hunters who are also fishermen in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

