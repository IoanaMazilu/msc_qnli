# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first more than 40 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: contradiction

hours_normal_pay_premise = 40
hours_normal_pay_hypothesis = 40

# the hypothesis talks about the number of hours James is paid x dollars, just like the premise
if hours_normal_pay_hypothesis <= hours_normal_pay_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a fixed value for the number of hours James is paid x dollars
    # any number of hours greater than 'hours_normal_pay_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

