# Premise: Each week, Harry is paid x dollars per hour for the first less than 80 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 30 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: neutral

first_hours_premise = 80
first_hours_hypothesis = 30

# the hypothesis talks about the number of hours Harry is paid x dollars per hour, referenced also in the premise
if first_hours_hypothesis >= first_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'first_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'first_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

