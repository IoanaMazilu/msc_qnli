premise_distance = 100
premise_time = 1
premise_speed = 46

hypothesis_distance = 100
hypothesis_time = 3
hypothesis_speed = 46

# the hypothesis refers to the same distance and time as the premise
if hypothesis_time == premise_time and hypothesis_distance == premise_distance:
    # check if the hypothesis speed contradicts the premise speed
    if hypothesis_speed!= premise_speed:
        label = "contradiction"
    else:
        label = "entailment"
else:
    # the hypothesis refers to a different distance or time than the premise
    label = "neutral"

print(label)
