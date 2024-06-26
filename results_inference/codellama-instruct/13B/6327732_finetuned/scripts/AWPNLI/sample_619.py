candy_bars_per_bag_premise = 5.0
number_of_bags_premise = 15.0
candy_bars_needed_hypothesis = 71.0

# the hypothesis refers to the total number of candy bars needed, which are also mentioned in the premise
# compute the total number of candy bars in the premise
total_candy_bars_premise = candy_bars_per_bag_premise * number_of_bags_premise
if candy_bars_needed_hypothesis!= total_candy_bars_premise:
    # check if the number of candy bars in the hypothesis contradicts the number of candy bars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
