# Premise: With the help of Pavan, they completed the work in 8 days and earned Rs.
# Hypothesis: With the help of Pavan, they completed the work in less than 8 days and earned Rs.
# Golden Label: contradiction

work_days_premise = 8
work_days_hypothesis = 8

# the hypothesis and premise both refer to the number of days taken to complete the work
if work_days_hypothesis < work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
elif work_days_hypothesis == work_days_premise:
    # if the number of days in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"
else:
    # if the number of days in the hypothesis is more than the premise, then it is neutral
    label = "neutral"

print(label)

