# Premise: Yesterday it took Robert less than 8 hours to drive from City A to City B.
# Hypothesis: Yesterday it took Robert 4 hours to drive from City A to City B.
# Golden Label: neutral

drive_time_premise = 8
drive_time_hypothesis = 4

# the hypothesis refers to the driving time from City A to City B mentioned in the premise
if drive_time_hypothesis >= drive_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time
    # any driving time less than 'drive_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

