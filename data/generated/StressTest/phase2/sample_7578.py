# Premise: With the help of Pavan, they completed the work in 8 days and earned Rs.
# Hypothesis: With the help of Pavan, they completed the work in more than 7 days and earned Rs.
# Golden Label: entailment

work_days_premise = 8
work_days_hypothesis = 7

# the hypothesis speaks about the number of days it took to complete the work, also mentioned in the premise
if work_days_premise < work_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of more than 'work_days_hypothesis'
    label = "contradiction"
elif work_days_premise == work_days_hypothesis:
    # check if the number of days in the premise is equal to 'work_days_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

