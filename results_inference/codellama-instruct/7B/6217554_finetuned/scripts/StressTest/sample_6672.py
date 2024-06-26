city_a_b_premise = 1
city_a_b_hypothesis = 5
speed_premise_1 = 40
speed_premise_2 = 60
speed_hypothesis_1 = 40
speed_hypothesis_2 = 60

# the hypothesis refers to the driving time and speed mentioned in the premise
if city_a_b_hypothesis <= city_a_b_premise:
    # check if the driving time in the hypothesis contradicts the driving time reported in the premise
    label = "contradiction"
elif speed_hypothesis_1!= speed_premise_1 or speed_hypothesis_2!= speed_premise_2:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
