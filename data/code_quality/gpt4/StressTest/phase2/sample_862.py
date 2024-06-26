percentage_premise = 20
percentage_hypothesis = 30
marks_obtained = 30
marks_failed_by = 36

# the hypothesis refers to the percentage of marks needed to pass the exam, which is also mentioned in the premise
if percentage_hypothesis <= percentage_premise:
    # check if the percentage value in the hypothesis contradicts the estimate of more than 'percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of marks needed to pass
    # a higher percentage needed to pass is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
