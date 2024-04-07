# Premise: Each week, Harry is paid x dollars per hour for the first less than 68 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 18 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: neutral

hours_premise = 68
hours_hypothesis = 18

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, which is also mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the number of hours in the hypothesis contradicts the estimate of less than 'hours_premise'
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

