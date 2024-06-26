yolanda_walking_rate_premise = 3
bob_walking_rate_premise = 4
yolanda_walking_rate_hypothesis = 5
bob_walking_rate_hypothesis = 4

# the hypothesis refers to the walking rates mentioned in the premise
if yolanda_walking_rate_hypothesis <= yolanda_walking_rate_premise:
    # check if the estimate of 'yolanda_walking_rate_hypothesis' contradicts the walking rate in the premise
    label = "contradiction"
elif bob_walking_rate_hypothesis!= bob_walking_rate_premise:
    # check if the walking rate in the hypothesis contradicts the walking rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
