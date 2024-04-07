# Premise: Each week, Harry is paid x dollars per hour for the first more than 11 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 21 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: neutral

hours_premise = 11
hours_hypothesis = 21

# Both the hypothesis and the premise talk about the number of hours for which Harry is paid x dollars
if hours_hypothesis <= hours_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of more than 'hours_premise' hours
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

