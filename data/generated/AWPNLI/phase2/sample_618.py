# Premise: Ted wants to put 5.0 candy bars in each of his 15.0 bags.
# Hypothesis: Ted needs to get 75.0 candy bars.
# Golden Label: entailment

candy_bars_per_bag_premise = 5.0
bags_premise = 15.0
total_candy_bars_hypothesis = 75.0

# the hypothesis refers to the total number of candy bars, which can be calculated from the premise
# compute the total number of candy bars in the premise
total_candy_bars_premise = candy_bars_per_bag_premise * bags_premise
if total_candy_bars_hypothesis != total_candy_bars_premise:
    # check if the number of candy bars in the hypothesis contradicts the number of candy bars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

