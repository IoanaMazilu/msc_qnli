cathy_speed_premise = 50
cathy_speed_hypothesis = 10
jim_speed_premise = 6
jim_speed_hypothesis = 6

# the hypothesis refers to the speeds of Cathy and Jim mentioned in the premise
if cathy_speed_hypothesis >= cathy_speed_premise:
    # check if the 'cathy_speed_hypothesis' contradicts the estimate of less than 'cathy_speed_premise'
    label = "contradiction"
elif jim_speed_hypothesis != jim_speed_premise:
    # check if the speed of Jim in the hypothesis contradicts the speed of Jim reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values are consistent with the premise ones, we can infer entailment
    label = "entailment"

print(label)
