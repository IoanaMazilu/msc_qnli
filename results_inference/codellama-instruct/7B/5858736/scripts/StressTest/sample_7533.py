# Define variables for the premise and hypothesis
premise_weight_gain = 10
sister_weight_difference = 50

# Define variables for the hypothesis
hypothesis_weight_gain = 50

# Check if the hypothesis weight gain is less than the premise weight gain
if hypothesis_weight_gain < premise_weight_gain:
    # Check if the weight difference between Leo and his sister is consistent with the hypothesis
    if (Leo_weight + hypothesis_weight_gain) / (sister_weight_difference / 100) > Kendra_weight:
        # The hypothesis is entailed from the premise
        label = "entailment"
    else:
        # The hypothesis is not entailed from the premise
        label = "contradiction"
else:
    # The hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
