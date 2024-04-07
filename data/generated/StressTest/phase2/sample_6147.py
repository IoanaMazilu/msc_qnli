# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first less than 70 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: entailment

hours_premise = 40
hours_hypothesis = 70
# the hypothesis talks about the number of hours James is paid x dollars for, referenced also in the premise
if hours_hypothesis > hours_premise:
    # check if the hypothesis value contradicts the estimate of 'hours_premise'
    label = "contradiction"
elif hours_hypothesis < hours_premise:
    # the premise gives a definite number of hours James is paid x dollars for
    # if the number of hours in the hypothesis is less than 'hours_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the number of hours in the hypothesis equals 'hours_premise', we can infer entailment
    label = "entailment"

print(label)

