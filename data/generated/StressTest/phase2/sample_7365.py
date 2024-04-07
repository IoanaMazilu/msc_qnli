# Premise: If Jack walked 7 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked more than 2 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: entailment

walking_distance_premise = 7
walking_distance_hypothesis = 2
walking_time_hours = 1.25  # 1 hour and 15 minutes converted to hours

# the hypothesis refers to the walking distance mentioned in the premise
if walking_distance_premise <= walking_distance_hypothesis:
    # check if the walking distance in the hypothesis contradicts the walking distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

