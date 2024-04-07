# Premise: Yesterday it took Robert 3 hours to drive from City A to City B.
# Hypothesis: Yesterday it took Robert more than 3 hours to drive from City A to City B.
# Golden Label: contradiction

drive_time_premise = 3
drive_time_hypothesis = 3

# the hypothesis refers to the time it took Robert to drive from City A to City B, which is also mentioned in the premise
if drive_time_hypothesis < drive_time_premise:
    # check if the hypothesis value contradicts the exact time reported in the premise
    label = "contradiction"
elif drive_time_hypothesis == drive_time_premise:
    # check if the hypothesis value is equal to the exact time reported in the premise
    label = "contradiction"
else:
    # the premise states an exact drive time
    # any drive time greater than 'drive_time_premise' contradicts the premise
    label = "neutral"

print(label)

