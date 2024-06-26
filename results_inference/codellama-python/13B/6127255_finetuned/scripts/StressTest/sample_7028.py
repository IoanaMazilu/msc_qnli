leave_time_premise = 120
leave_time_hypothesis = 120

# the hypothesis refers to the time difference between Dan and Cara leaving City A
if leave_time_hypothesis <= leave_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact time difference
    # any time difference greater than 'leave_time_premise' contradicts the premise
    label = "contradiction"

print(label)
