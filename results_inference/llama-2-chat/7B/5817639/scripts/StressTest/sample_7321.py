gym_attendance_premise = 6
gym_attendance_hypothesis = 3

# the hypothesis talks about the number of weeks Rikki went to the gym, referenced also in the premise
if gym_attendance_hypothesis <= gym_attendance_premise:
    # check if the hypothesis value contradicts the estimate of 'gym_attendance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks,
    # any number of weeks greater than 'gym_attendance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
