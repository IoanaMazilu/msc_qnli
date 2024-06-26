drive_time_premise = 4
drive_time_hypothesis = 8

# the hypothesis refers to the driving time from City A to City B mentioned in the premise
if drive_time_premise > drive_time_hypothesis:
    # check if the driving time in the premise contradicts the estimate of less than 'drive_time_hypothesis'
    label = "contradiction"
elif drive_time_premise < drive_time_hypothesis:
    # check if the driving time in the premise is less than the 'drive_time_hypothesis'
    label = "entailment"
else:
    # if the driving time in the premise is equal to the 'drive_time_hypothesis', it is consistent with the hypothesis but cannot be explicitly entailed from it
    label = "neutral"

print(label)
