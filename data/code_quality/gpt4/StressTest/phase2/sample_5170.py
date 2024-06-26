cathy_speed_premise = 70
cara_speed_premise = 5
cathy_speed_hypothesis = 10
cara_speed_hypothesis = 5

# the hypothesis refers to the running speed of Cathy and Cara mentioned in the premise
if cathy_speed_hypothesis >= cathy_speed_premise:
    # check if 'cathy_speed_hypothesis' contradicts the premise that Cathy runs at less than 'cathy_speed_premise'
    label = "contradiction"
elif cara_speed_hypothesis != cara_speed_premise:
    # check if the speed of Cara in the hypothesis contradicts the speed of Cara reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
