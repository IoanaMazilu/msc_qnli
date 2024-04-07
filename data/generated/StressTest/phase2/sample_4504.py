# Premise: Each week, Harry is paid x dollars per hour for the first less than 65 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 15 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: neutral

first_hours_premise = 65
first_hours_hypothesis = 15

# the hypothesis talks about the hours Harry is paid x dollars per hour, referenced also in the premise
if first_hours_hypothesis >= first_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'first_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the first hours paid x dollars per hour
    # any number of hours less than 'first_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

