city_a_to_b_speed_premise = 30
city_b_to_c_speed_premise = 60
city_a_to_b_speed_hypothesis = 40
city_b_to_c_speed_hypothesis = 60

# the hypothesis refers to the speed of travel between two cities, mentioned in the premise
if city_a_to_b_speed_hypothesis <= city_a_to_b_speed_premise:
    # check if the estimate of 'city_a_to_b_speed_hypothesis' contradicts the speed of travel in the premise
    label = "contradiction"
elif city_b_to_c_speed_hypothesis!= city_b_to_c_speed_premise:
    # check if the speed of travel in the hypothesis contradicts the speed of travel in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
