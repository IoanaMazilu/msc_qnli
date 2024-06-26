leave_time_premise = 120
leave_time_hypothesis = 120

# the hypothesis refers to the time Dan leaves City A after Cara, mentioned in the premise
if leave_time_hypothesis <= leave_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact time for Dan's departure
    # any departure time greater than 'leave_time_premise' contradicts the premise
    label = "contradiction"

print(label)
