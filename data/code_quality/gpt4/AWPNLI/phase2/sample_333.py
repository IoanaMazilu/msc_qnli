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
