speed_home_to_beach_premise = 80
speed_home_to_beach_hypothesis = 60
speed_beach_to_home_premise = 70
speed_beach_to_home_hypothesis = 70

# the hypothesis refers to the average speeds of Carl's trip to the beach and back home
if speed_home_to_beach_premise!= speed_home_to_beach_hypothesis:
    # check if the speed of driving from home to the beach in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif speed_beach_to_home_premise!= speed_beach_to_home_hypothesis:
    # check if the speed of driving from the beach to home in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
