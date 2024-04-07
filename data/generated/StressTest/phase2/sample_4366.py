# Premise: Each week, James is paid x dollars per per hour for the first less than 60 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: neutral

regular_hours_premise = 60
regular_hours_hypothesis = 40

# the hypothesis talks about the number of regular hours James is paid x dollars for, also mentioned in the premise
if regular_hours_hypothesis >= regular_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'regular_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of regular hours
    # any number of regular hours less than 'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

