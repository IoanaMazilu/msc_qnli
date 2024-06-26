average_speed_home_to_beach_premise = 80
average_speed_home_to_beach_hypothesis = 80
average_speed_return_home_premise = 70
average_speed_return_home_hypothesis = 70

# the hypothesis refers to the average speed of Carl's drive from home to the beach and return home
if average_speed_home_to_beach_hypothesis <= average_speed_home_to_beach_premise:
    # check if the hypothesis value contradicts the premise value of more than 'average_speed_home_to_beach_premise'
    label = "contradiction"
elif average_speed_return_home_hypothesis!= average_speed_return_home_premise:
    # check if the hypothesis value contradicts the premise value of 'average_speed_return_home_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
