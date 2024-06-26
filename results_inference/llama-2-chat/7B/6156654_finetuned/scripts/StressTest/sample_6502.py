matthew_walking_rate_premise = 5
matthew_walking_rate_hypothesis = 3
johnny_walking_rate_premise = 4
johnny_walking_rate_hypothesis = 4

# the hypothesis talks about the walking rate of Matthew and Johnny, which is also mentioned in the premise
if matthew_walking_rate_hypothesis!= matthew_walking_rate_premise:
    # check if the walking rate of Matthew in the hypothesis contradicts the walking rate of Matthew in the premise
    label = "contradiction"
elif johnny_walking_rate_hypothesis!= johnny_walking_rate_premise:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny in the premise
    label = "contradiction"
else:
    # if the walking rates of Matthew and Johnny in the hypothesis do not contradict the walking rates in the premise, we can infer entailment
    label = "entailment"

print(label)
