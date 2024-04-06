# Premise: The two Marines on the Marine Corps Base Camp Pendleton chopper were one of four helicopter crews involved in the training exercise, Stevens said.
# Hypothesis: The Marine helicopter contained two crew members.
# Golden Label: neutral

crew_premise = 2
crew_hypothesis = 2

# the hypothesis mentions the number of crew members on the helicopter, which is also mentioned in the premise
if crew_hypothesis != crew_premise:
    # check if the number of crew members in the hypothesis contradicts the number of crew members in the premise
    label = "contradiction"
else:
    # if the number of crew members in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

