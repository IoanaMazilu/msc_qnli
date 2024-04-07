# Premise: Jhon works for 60 days.
# Hypothesis: Jhon works for less than 60 days.
# Golden Label: contradiction

work_days_premise = 60
work_days_hypothesis = 60

# the hypothesis talks about the number of days John works, referenced also in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the value of 'work_days_hypothesis' is less than 'work_days_premise', we can infer entailment
    label = "entailment"

print(label)

