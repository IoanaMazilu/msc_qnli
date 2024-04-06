# Premise: Three people were initially reported to be on board the helicopter, Lunsford said.
# Hypothesis: Three crew members, no patients were on board.
# Golden Label: neutral

people_onboard_premise = 3
people_onboard_hypothesis = 3

# the hypothesis mentions the number of people on board the helicopter which is also mentioned in the premise
if people_onboard_hypothesis != people_onboard_premise:
    # check if the number of people on board in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

