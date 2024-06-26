dawson_first_leg_premise = 38
dawson_first_leg_hypothesis = 68

# the hypothesis refers to the time taken by Dawson to run the first leg of the course, which is also mentioned in the premise
if dawson_first_leg_hypothesis <= dawson_first_leg_premise:
    # check if the estimate of 'dawson_first_leg_hypothesis' contradicts the time taken by Dawson in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
