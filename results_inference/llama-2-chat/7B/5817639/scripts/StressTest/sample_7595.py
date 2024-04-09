# Define variables for the entities in the input sentences
premise_time = 60
hypothesis_time = 70

# Compare the variables to determine the relation between the premise and hypothesis
if hypothesis_time <= premise_time:
    # If the hypothesis time is less than or equal to the premise time, it contradicts the premise
    label = "contradiction"
elif hypothesis_time > premise_time:
    # If the hypothesis time is greater than the premise time, it entails the premise
    label = "entailment"
else:
    # If the hypothesis time is neither greater nor less than the premise time, it is neutral
    label = "neutral"

print(label)
