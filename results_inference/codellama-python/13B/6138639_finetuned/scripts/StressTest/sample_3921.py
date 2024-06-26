# Define the variables for the premise and hypothesis
departure_time_premise = 9
departure_time_hypothesis = 4

# The hypothesis refers to the departure time of a train from Delhi mentioned in the premise
if departure_time_premise <= departure_time_hypothesis:
    # Check if the hypothesis value contradicts the departure time in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)