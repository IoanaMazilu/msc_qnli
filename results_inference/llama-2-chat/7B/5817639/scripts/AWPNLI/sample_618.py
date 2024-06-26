candy_bars_premise = 5.0
bags_premise = 15.0
candy_bars_hypothesis = 75.0

# the hypothesis refers to the total number of candy bars, which is also mentioned in the premise
# compute the total number of candy bars in the premise
total_candy_bars_premise = candy_bars_premise * bags_premise

# check if the number of candy bars in the hypothesis contradicts the number of candy bars from the premise
if total_candy_bars_hypothesis!= total_candy_bars_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)