# Premise: Kamal will complete work in 20 days.
# Hypothesis: Kamal will complete work in more than 20 days.
# Golden Label: contradiction

work_completion_days_premise = 20
work_completion_days_hypothesis = 20

# the hypothesis talks about the time Kamal will take to complete work, which is also mentioned in the premise
if work_completion_days_hypothesis != work_completion_days_premise:
    # check if the hypothesis value contradicts the estimate of 'work_completion_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days equal to 'work_completion_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

