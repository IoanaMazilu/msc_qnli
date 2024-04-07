# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first less than 60 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: entailment

hours_normal_pay_premise = 40
hours_normal_pay_hypothesis = 60
additional_pay_premise = 2
additional_pay_hypothesis = 2

# the hypothesis talks about the number of hours James is paid x dollars per hour and the additional pay per hour after a certain number of hours, both referenced in the premise
if hours_normal_pay_hypothesis <= hours_normal_pay_premise:
    # check if the hypothesis value contradicts the number of hours James is paid x dollars per hour in the premise
    label = "contradiction"
elif additional_pay_hypothesis != additional_pay_premise:
    # check if the additional pay per hour in the hypothesis contradicts the additional pay per hour in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of hours James is paid x dollars per hour and the additional pay per hour after that
    # any number of hours greater than 'hours_normal_pay_premise' for the normal pay is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

