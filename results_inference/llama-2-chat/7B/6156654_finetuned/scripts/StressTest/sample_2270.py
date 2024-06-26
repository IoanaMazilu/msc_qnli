speed_from_city_a_to_city_b_premise = 40
speed_from_city_b_to_city_c_premise = 60
speed_from_city_b_to_city_c_hypothesis = 80

# the hypothesis talks about the speed of travel from city B to city C, which is also mentioned in the premise
if speed_from_city_b_to_city_c_hypothesis!= speed_from_city_b_to_city_c_premise:
    label = "contradiction"
elif speed_from_city_b_to_city_c_hypothesis > speed_from_city_b_to_city_c_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
