# Premise: Suresh works for more than 1 hours and then the remaining job is completed by Ashutosh.
# Hypothesis: Suresh works for 9 hours and then the remaining job is completed by Ashutosh.
# Golden Label: neutral

work_hours_suresh_premise = 1
work_hours_suresh_hypothesis = 9

# the hypothesis talks about the number of hours Suresh works, referenced also in the premise
if work_hours_suresh_hypothesis <= work_hours_suresh_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_suresh_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Suresh works
    # any number of hours greater than 'work_hours_suresh_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

