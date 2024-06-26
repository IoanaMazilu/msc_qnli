subjects_premise = [50, 60, 70, 80, 80]
subjects_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis talks about the average of different subjects, which is also referred to in the premise
if sum(subjects_hypothesis) <= sum(subjects_premise):
    # check if the estimate of the average in the hypothesis contradicts the estimate of the average in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average, and any estimate greater than that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
