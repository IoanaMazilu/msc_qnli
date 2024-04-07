# Premise: Each week, Harry is paid x dollars per hour for the first 30 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first more than 10 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

hours_rate_premise = 30
hours_rate_hypothesis = 10
additional_rate_premise = 1.5
additional_rate_hypothesis = 1.5

# the hypothesis refers to the hours and rates Harry is paid per week, which are also mentioned in the premise
if hours_rate_hypothesis > hours_rate_premise:
    # check if the hypothesis estimate contradicts the number of hours Harry is paid x dollars per hour in the premise
    label = "contradiction"
elif additional_rate_hypothesis != additional_rate_premise:
    # check if the rate for the additional hours in the hypothesis contradicts the rate for the additional hours in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of hours Harry is paid x dollars per hour and the rate for additional hours
    # any number of hours less than or equal to 'hours_rate_premise' and the same rate for additional hours can be explicitly entailed from the premise
    label = "entailment"

print(label)

