# Premise: Each week, Harry is paid x dollars per hour for the first more than 10 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 30 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: neutral

hours_paid_premise = 10
hours_paid_hypothesis = 30

# the hypothesis talks about the same situation as the premise, but with different numbers of hours
if hours_paid_hypothesis <= hours_paid_premise:
    # check if the hypothesis value contradicts the premise, which specifies 'more than 10 hours'
    label = "contradiction"
else:
    # the premise gives only a lower limit for the number of hours
    # any number of hours greater than 'hours_paid_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

