home_to_beach_speed_premise = 80
home_to_beach_speed_hypothesis = 60
return_home_speed_premise = 70
return_home_speed_hypothesis = 70

# the hypothesis refers to the average speed of Carl's journey from his home to the beach and his return home
if home_to_beach_speed_hypothesis >= home_to_beach_speed_premise:
    # check if the hypothesis value contradicts the estimate of 'home_to_beach_speed_premise'
    label = "contradiction"
elif return_home_speed_hypothesis!= return_home_speed_premise:
    # check if the hypothesis value contradicts the estimate of'return_home_speed_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
