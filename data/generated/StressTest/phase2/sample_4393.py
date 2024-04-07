# Premise: Each week, James is paid x dollars per per hour for the first more than 30 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: neutral

hours_premise = 30
hours_hypothesis = 40

# the hypothesis talks about the hours of work that James is paid "x" dollars for, which is also referenced in the premise
if hours_hypothesis <= hours_premise:
    # check if the hours in the hypothesis contradict the estimate of more than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

