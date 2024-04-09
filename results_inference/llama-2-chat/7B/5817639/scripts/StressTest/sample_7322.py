gym_attendance_premise = 2 * 3 = 6
gym_attendance_hypothesis = 2

# the hypothesis refers to the number of times Rikki went to the gym in a specific week, which is also mentioned in the premise
if gym_attendance_premise <= gym_attendance_hypothesis:
    # check if the estimate of 'gym_attendance_hypothesis' contradicts the average number of gym attendances in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average number of gym attendances, which is consistent with the hypothesis
    label = "entailment"

print(label)
