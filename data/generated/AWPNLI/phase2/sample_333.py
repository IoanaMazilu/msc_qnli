# Premise: Lewis saved checking on the grapevines for his last stop and he was told by 1.0 of the pickers that they fill 324.0 drums of grapes per day.
# Hypothesis: 2914.0 drums of grapes would be filled in 9.0 days.
# Golden Label: contradiction

drums_per_day_premise = 324.0
total_drums_hypothesis = 2914.0
total_days_hypothesis = 9.0

# the hypothesis refers to the total amount of drums filled in a certain number of days
# compute the total amount of drums in the premise for the same number of days
total_drums_premise = drums_per_day_premise * total_days_hypothesis
if total_drums_hypothesis != total_drums_premise:
    # check if the total drums in the hypothesis contradicts the total drums from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
