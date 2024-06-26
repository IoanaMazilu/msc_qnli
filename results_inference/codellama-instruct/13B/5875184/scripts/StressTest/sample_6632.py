premise_distance = 500
premise_speed = 15
hypothesis_distance = 500
hypothesis_speed = 15

# the hypothesis refers to a distance greater than the premise distance
if hypothesis_distance > premise_distance:
    # check if the hypothesis speed contradicts the premise speed
    if hypothesis_speed!= premise_speed:
        label = "contradiction"
    else:
        label = "entailment"
else:
    label = "neutral"

print(label)
