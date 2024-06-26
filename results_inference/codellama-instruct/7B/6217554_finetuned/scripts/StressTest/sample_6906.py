city_a_b_premise = 1
city_a_b_hypothesis = 2
andrew_speed_premise_1 = 44
andrew_speed_premise_2 = 60
andrew_speed_hypothesis_1 = 44
andrew_speed_hypothesis_2 = 60

# the hypothesis refers to the driving time and speed mentioned in the premise
if city_a_b_hypothesis >= city_a_b_premise:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
elif andrew_speed_hypothesis_1!= andrew_speed_premise_1 or andrew_speed_hypothesis_2!= andrew_speed_premise_2:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
