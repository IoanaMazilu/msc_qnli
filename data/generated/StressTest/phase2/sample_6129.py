# Premise: Each week, Harry is paid x dollars per hour for the first 21 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first more than 11 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

regular_hours_premise = 21
regular_hours_hypothesis = 11

# the hypothesis talks about the number of regular hours Harry is paid x dollars for, which is also referenced in the premise
if regular_hours_hypothesis >= regular_hours_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific number of regular hours
    # any number of regular hours less than 'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

