work_days_premise = 35
work_days_hypothesis = 25

# the hypothesis talks about the number of days it would take for Sreedhar and Sravan to complete a work, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
