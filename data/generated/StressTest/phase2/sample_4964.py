# Premise: Suresh works for 9 hours and then the remaining job is completed by Ashutosh.
# Hypothesis: Suresh works for less than 9 hours and then the remaining job is completed by Ashutosh.
# Golden Label: contradiction

suresh_work_hours_premise = 9
suresh_work_hours_hypothesis = 9

# the hypothesis talks about the number of hours Suresh works, referenced also in the premise
if suresh_work_hours_hypothesis >= suresh_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of 'suresh_work_hours_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than 'suresh_work_hours_premise', we can infer entailment
    label = "entailment"

print(label)

