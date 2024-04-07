# Premise: Suresh works for more than 6 hours and then the remaining job is completed by Ashutosh.
# Hypothesis: Suresh works for 9 hours and then the remaining job is completed by Ashutosh.
# Golden Label: neutral

suresh_work_hours_premise = 6
suresh_work_hours_hypothesis = 9

# the hypothesis refers to the number of hours Suresh works, mentioned also in the premise
if suresh_work_hours_hypothesis <= suresh_work_hours_premise:
    # check if the number of hours Suresh works in the hypothesis contradicts the estimated number of hours in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Suresh works
    # any number of hours greater than 'suresh_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

