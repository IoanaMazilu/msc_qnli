# Define variables for the premise and hypothesis
premise_speed_home_to_beach = 80
premise_speed_home_to_beach_return = 70
hypothesis_speed_home_to_beach = 40

# Check if the hypothesis speed is greater than the premise speed
if hypothesis_speed_home_to_beach > premise_speed_home_to_beach:
    # Check if the hypothesis speed is consistent with the premise speed
    if hypothesis_speed_home_to_beach == premise_speed_home_to_beach_return:
        # The hypothesis is consistent with the premise, so the label is entailment
        label = "entailment"
    else:
        # The hypothesis speed is greater than the premise speed, but it is not consistent with the premise speed, so the label is contradiction
        label = "contradiction"
else:
    # The hypothesis speed is less than or equal to the premise speed, so the label is neutral
    label = "neutral"

print(label)
