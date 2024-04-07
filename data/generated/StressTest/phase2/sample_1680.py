# Premise: Suresh works for 9 hours and then the remaining job is completed by Ashutosh.
# Hypothesis: Suresh works for more than 7 hours and then the remaining job is completed by Ashutosh.
# Golden Label: entailment

suresh_work_hours_premise = 9
suresh_work_hours_hypothesis = 7

# the hypothesis refers to the number of hours Suresh works, which is also mentioned in the premise
if suresh_work_hours_premise <= suresh_work_hours_hypothesis:
    # check if the estimate of 'suresh_work_hours_hypothesis' contradicts the number of hours Suresh works in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

