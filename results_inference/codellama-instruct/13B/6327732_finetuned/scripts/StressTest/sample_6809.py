yolanda_walking_rate_premise = 3
yolanda_walking_rate_hypothesis = 5
bob_walking_rate_premise = 4
bob_walking_rate_hypothesis = 4

# the hypothesis refers to the walking rates mentioned in the premise
if yolanda_walking_rate_hypothesis!= yolanda_walking_rate_premise:
    # check if the hypothesis value contradicts the premise value for Yolanda's walking rate
    label = "contradiction"
elif bob_walking_rate_hypothesis!= bob_walking_rate_premise:
    # check if the hypothesis value contradicts the premise value for Bob's walking rate
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
