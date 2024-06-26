# Define variables for the premise and hypothesis
premise_epicenter = "Negros"
hypothesis_epicenter = "Negros"
premise_distance = 360
hypothesis_distance = 360

# Check if the epicenter of the quake in the hypothesis is the same as in the premise
if hypothesis_epicenter == premise_epicenter:
    # Check if the distance between the epicenter of the quake in the hypothesis is the same as in the premise
    if hypothesis_distance == premise_distance:
        # If both conditions are true, we can infer entailment
        label = "entailment"
    else:
        # If the distance between the epicenter of the quake in the hypothesis is not the same as in the premise, we can infer contradiction
        label = "contradiction"
else:
    # If the epicenter of the quake in the hypothesis is not the same as in the premise, we can infer neutral
    label = "neutral"

print(label)
