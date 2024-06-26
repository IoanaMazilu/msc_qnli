average_speed_from_home_to_beach = 80
average_speed_from_beach_to_home = 70

# the hypothesis refers to the average speed of Carl's journey from home to beach and back, which is also mentioned in the premise
if average_speed_from_home_to_beach <= average_speed_from_beach_to_home:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
