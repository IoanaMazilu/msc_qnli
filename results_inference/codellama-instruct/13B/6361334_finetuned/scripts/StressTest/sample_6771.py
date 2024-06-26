city_a_to_b_speed_premise = 40
city_b_to_c_speed_premise = 60
city_a_to_b_speed_hypothesis = 50
city_b_to_c_speed_hypothesis = 60

# the hypothesis refers to the speed of travel from city A to city B and from city B to city C, which are also mentioned in the premise
if city_a_to_b_speed_hypothesis >= city_a_to_b_speed_premise:
    # check if the estimate of 'city_a_to_b_speed_hypothesis' contradicts the speed of travel from city A to city B in the premise
    label = "contradiction"
elif city_b_to_c_speed_hypothesis!= city_b_to_c_speed_premise:
    # check if the speed of travel from city B to city C in the hypothesis contradicts the speed of travel from city B to city C reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
