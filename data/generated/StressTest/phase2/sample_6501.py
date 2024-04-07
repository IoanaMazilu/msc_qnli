# Premise: Matthew's walking rate was 3 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Hypothesis: Matthew's walking rate was less than 5 km per hour and Johnny's was 4 km per hour, how many km had Johnny walked when they met?
# Golden Label: entailment

matthew_rate_premise = 3
johnny_rate_premise = 4
matthew_rate_hypothesis = 5
johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny, which were also mentioned in the premise
if matthew_rate_hypothesis < matthew_rate_premise:
    # check if the estimate of 'matthew_rate_hypothesis' contradicts the walking rate of Matthew in the premise
    label = "contradiction"
elif johnny_rate_hypothesis != johnny_rate_premise:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
