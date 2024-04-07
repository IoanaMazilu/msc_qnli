# Premise: If Jack walked 9 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Hypothesis: If Jack walked more than 9 miles in 1 hour and 15 minutes, what was his rate of walking in miles per hour?
# Golden Label: contradiction

walk_distance_premise = 9
walk_time_premise = 1.25  # 1 hour and 15 minutes is 1.25 hours
walk_distance_hypothesis = 9

# the hypothesis refers to the distance Jack walked in a certain time, which is also mentioned in the premise
if walk_distance_hypothesis > walk_distance_premise:
    # check if the hypothesis value contradicts the exact distance Jack walked in the premise
    label = "contradiction"
else:
    # the premise gives the exact distance Jack walked
    # the distance in the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

