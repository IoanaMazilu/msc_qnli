# Premise: 30% of all fishermen in Piscataquis County are also hunters while only 20% of all hunters are fishermen.
# Hypothesis: less than 50% of all fishermen in Piscataquis County are also hunters while only 20% of all hunters are fishermen.
# Golden Label: entailment

fishermen_hunters_premise = 30
fishermen_hunters_hypothesis = 50
hunters_fishermen_premise = 20
hunters_fishermen_hypothesis = 20

# the hypothesis refers to the percentages of fishermen that are hunters and hunters that are fishermen, as mentioned in the premise
if fishermen_hunters_hypothesis < fishermen_hunters_premise:
    # check if the hypothesized percentage of fishermen that are hunters contradicts the premise
    label = "contradiction"
elif hunters_fishermen_hypothesis != hunters_fishermen_premise:
    # check if the hypothesized percentage of hunters that are fishermen contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

