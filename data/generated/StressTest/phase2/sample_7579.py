# Premise: With the help of Pavan, they completed the work in more than 7 days and earned Rs.
# Hypothesis: With the help of Pavan, they completed the work in 8 days and earned Rs.
# Golden Label: neutral

work_days_premise = 7
work_days_hypothesis = 8

# the hypothesis talks about the number of days it took to complete the work, referenced also in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

