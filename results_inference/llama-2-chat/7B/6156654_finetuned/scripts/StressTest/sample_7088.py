work_hours_dan = 6
work_hours_dan_hypothesis = 6
work_hours_dan_premise = 6

# The hypothesis talks about Dan's work hours, which are also mentioned in the premise
if work_hours_dan_hypothesis >= work_hours_dan_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
