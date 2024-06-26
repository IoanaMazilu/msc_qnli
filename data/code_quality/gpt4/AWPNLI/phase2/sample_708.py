harvest_days_premise = 6.0
sacks_oranges_premise = 83.0
sacks_per_day_hypothesis = 13.8333333333

# the hypothesis refers to the number of sacks harvested per day
# compute the number of sacks harvested per day in the premise
sacks_per_day_premise = sacks_oranges_premise / harvest_days_premise
if sacks_per_day_hypothesis != sacks_per_day_premise:
    # check if the number of sacks per day in the hypothesis contradicts the number of sacks per day from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
