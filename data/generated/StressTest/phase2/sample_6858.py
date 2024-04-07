# Premise: If Jack walked 4 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked more than 3 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: entailment

distance_premise = 4
distance_hypothesis = 3
time_premise = 1.25 # 1 hour and 15 minutes
time_hypothesis = 1.25 # 1 hour and 15 minutes

# The hypothesis refers to the distance Jack walked and the time he did it in, which are also mentioned in the premise
if distance_premise <= distance_hypothesis:
    # Check if the distance in the hypothesis contradicts the distance walked in the premise
    label = "contradiction"
elif time_hypothesis != time_premise:
    # Check if the time in the hypothesis contradicts the time walked in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

