cathy_speed_premise = 10
cara_speed_premise = 5
cathy_speed_hypothesis = 70
cara_speed_hypothesis = 5

# the hypothesis refers to the speeds of Cathy and Cara mentioned in the premise
if cathy_speed_premise >= cathy_speed_hypothesis:
    # check if the 'cathy_speed_premise' contradicts the estimate of less than 'cathy_speed_hypothesis'
    label = "contradiction"
elif cara_speed_hypothesis != cara_speed_premise:
    # check if the speed of Cara in the hypothesis contradicts the speed of Cara reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
