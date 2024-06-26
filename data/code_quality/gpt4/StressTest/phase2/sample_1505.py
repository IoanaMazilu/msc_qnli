cathy_speed_premise = 10
cathy_speed_hypothesis = 30
jim_speed_premise = 6
jim_speed_hypothesis = 6

# the hypothesis refers to the running speeds of Cathy and Jim, mentioned in the premise
if cathy_speed_hypothesis != cathy_speed_premise:
    # check if Cathy's speed in the hypothesis contradicts her speed reported in the premise
    label = "contradiction"
elif jim_speed_hypothesis != jim_speed_premise:
    # check if Jim's speed in the hypothesis contradicts his speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
