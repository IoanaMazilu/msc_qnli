premise_distance = 8
premise_speed = 40
premise_stop_time = 15
premise_additional_distance = 20
premise_additional_speed = 60

hypothesis_distance = 7
hypothesis_speed = 40
hypothesis_stop_time = 15
hypothesis_additional_distance = 20
hypothesis_additional_speed = 60

# check if the hypothesis distance is greater than the premise distance
if hypothesis_distance > premise_distance:
    # check if the hypothesis speed is greater than the premise speed
    if hypothesis_speed > premise_speed:
        # check if the hypothesis stop time is equal to the premise stop time
        if hypothesis_stop_time == premise_stop_time:
            # check if the hypothesis additional distance is equal to the premise additional distance
            if hypothesis_additional_distance == premise_additional_distance:
                # check if the hypothesis additional speed is greater than the premise additional speed
                if hypothesis_additional_speed > premise_additional_speed:
                    label = "entailment"
                else:
                    label = "contradiction"
            else:
                label = "contradiction"
        else:
            label = "contradiction"
    else:
        label = "contradiction"
else:
    label = "neutral"

print(label)
