premise_distance = 20
premise_maxwell_speed = 4
premise_brad_speed = 6

hypothesis_distance = 20
hypothesis_maxwell_speed = 4
hypothesis_brad_speed = 6

# check if the hypothesis distance is greater than the premise distance
if hypothesis_distance > premise_distance:
    # check if the hypothesis maxwell speed is less than the premise maxwell speed
    if hypothesis_maxwell_speed < premise_maxwell_speed:
        # check if the hypothesis brad speed is less than the premise brad speed
        if hypothesis_brad_speed < premise_brad_speed:
            # if all the conditions are met, we can infer entailment
            label = "entailment"
        else:
            # if the hypothesis brad speed is not less than the premise brad speed, we can infer contradiction
            label = "contradiction"
    else:
        # if the hypothesis maxwell speed is not less than the premise maxwell speed, we can infer contradiction
        label = "contradiction"
else:
    # if the hypothesis distance is not greater than the premise distance, we can infer neutral
    label = "neutral"

print(label)
