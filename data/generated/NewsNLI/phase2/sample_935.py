# Premise: Despite design improvements, warnings and instructions to the company's Generation Two model and Nap Nanny Chill recliner, there have been four more fatalities, the CPSC alleged.
# Hypothesis: Five infant deaths have been linked to the recliners, the government says.
# Golden Label: neutral

fatalities_premise = 4
fatalities_hypothesis = 5

# the hypothesis mentions the number of infant deaths linked to the recliners, which is also mentioned in the premise
if fatalities_hypothesis > fatalities_premise:
    # check if the number of fatalities in the hypothesis contradicts the number of fatalities reported in the premise
    label = "contradiction"
else:
    # if the number of fatalities in the hypothesis does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

