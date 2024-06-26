ratio_sheep_horses_premise = 4/7
ratio_sheep_horses_hypothesis = 3/7
horse_feed_per_day_premise = 230
horse_feed_per_day_hypothesis = 230
total_horse_feed_premise = 12880
total_horse_feed_hypothesis = 12880

# the hypothesis talks about the ratio of sheep to horses, and the amount of horse feed used daily at the Stewart farm, same as the premise
if (ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise) or (horse_feed_per_day_hypothesis != horse_feed_per_day_premise) or (total_horse_feed_hypothesis != total_horse_feed_premise):
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    # also, check if either the total horse feed or the horse feed per day in the hypothesis contradicts the respective numbers in the premise
    label = "contradiction"
else:
    # if the ratio and the numbers in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
