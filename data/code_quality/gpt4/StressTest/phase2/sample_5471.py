sheep_to_horse_ratio_premise = 3 / 7
horse_feed_per_day = 230
total_horse_feed_needed_per_day = 12880
sheep_to_horse_ratio_hypothesis = 3 / 7

# The number of horses on the farm can be calculated from the total amount of horse food needed and the feed per horse per day
horses_premise = total_horse_feed_needed_per_day / horse_feed_per_day

# The number of sheep on the farm can be calculated using the sheep to horse ratio and the number of horses
sheep_premise = sheep_to_horse_ratio_premise * horses_premise

# The hypothesis refers to the ratio of sheep to horses, which is also mentioned in the premise
if sheep_to_horse_ratio_hypothesis > sheep_to_horse_ratio_premise:
    # check if the sheep to horse ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
