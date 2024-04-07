# Premise: Matthew's walking rate was 3 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Hypothesis: Matthew's walking rate was 8 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Golden Label: contradiction

matthew_speed_premise = 3
johnny_speed_premise = 4
matthew_speed_hypothesis = 8
johnny_speed_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
if matthew_speed_premise != matthew_speed_hypothesis:
    # check if the walking rate of Matthew in the hypothesis contradicts the walking rate of Matthew in the premise
    label = "contradiction"
elif johnny_speed_premise != johnny_speed_hypothesis:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny in the premise
    label = "contradiction"
else:
    # if the walking rates in the hypothesis do not contradict the walking rates in the premise, we can infer entailment
    label = "entailment"

print(label)

