candy_bars_premise = float(5.0)
bags_premise = float(15.0)
candy_bars_hypothesis = float(71.0)

# the hypothesis talks about the number of candy bars, which is also mentioned in the premise
# compute the total number of candy bars in the premise
total_candy_bars_premise = candy_bars_premise * bags_premise

# check if the number of candy bars in the hypothesis contradicts the number of candy bars from the premise
if candy_bars_hypothesis!= total_candy_bars_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
