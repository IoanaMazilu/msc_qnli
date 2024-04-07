# Premise: Each week, Harry is paid x dollars per hour for the first less than 82 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 12 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: neutral

hours_normal_rate_premise = 82
hours_normal_rate_hypothesis = 12

# the hypothesis refers to the hours worked at normal rate, also mentioned in the premise
if hours_normal_rate_hypothesis >= hours_normal_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_normal_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked at normal rate
    # any number of hours worked less than 'hours_normal_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

