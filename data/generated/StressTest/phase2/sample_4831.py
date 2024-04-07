# Premise: Matthew's walking rate was more than 1 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Hypothesis: Matthew's walking rate was 3 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Golden Label: neutral

matthew_rate_premise = 1
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# The hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
if matthew_rate_hypothesis <= matthew_rate_premise:
    # check if the value of 'matthew_rate_hypothesis' contradicts the estimate in the premise
    label = "contradiction"
elif johnny_rate_hypothesis != johnny_rate_premise:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, but also cannot be fully entailed, the logical relation is neutral
    label = "neutral"

print(label)

