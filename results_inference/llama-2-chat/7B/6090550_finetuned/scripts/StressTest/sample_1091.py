matthew_rate_premise = 3
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny
if matthew_rate_premise > matthew_rate_hypothesis:
    # check if Matthew's rate in the hypothesis contradicts Matthew's rate in the premise
    label = "contradiction"
elif johnny_rate_hypothesis!= johnny_rate_premise:
    # check if Johnny's rate in the hypothesis contradicts Johnny's rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
