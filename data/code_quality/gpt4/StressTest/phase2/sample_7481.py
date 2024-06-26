first_hours_premise = 24
first_hours_hypothesis = 54

# the hypothesis talks about the number of hours Harry is paid x dollars per hour each week, referenced also in the premise
if first_hours_hypothesis == first_hours_premise:
    # check if the number of first_hours_hypothesis contradicts the first_hours_premise
    label = "entailment"
elif first_hours_hypothesis < first_hours_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific number of hours Harry is paid x dollars per hour each week
    # any number of hours greater than 'first_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
