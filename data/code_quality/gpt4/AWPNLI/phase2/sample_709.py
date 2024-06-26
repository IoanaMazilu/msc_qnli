days_premise = 6.0
sacks_premise = 83.0
sacks_per_day_hypothesis = 18.0

# the hypothesis talks about the number of sacks harvested per day, which can be inferred from the premise
# calculate the number of sacks harvested per day from the premise
sacks_per_day_premise = sacks_premise / days_premise
if sacks_per_day_hypothesis != sacks_per_day_premise:
    # check if the number of sacks per day from the hypothesis contradicts the number of sacks per day from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
