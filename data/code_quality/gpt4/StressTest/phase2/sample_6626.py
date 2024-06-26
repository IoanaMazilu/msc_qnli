ratio_premise = 6 / 7
horse_feed_per_day = 230
total_horse_feed_day = 12880

ratio_hypothesis = 5 / 7

# The hypothesis talks about the ratio of sheep to horses on the Stewart farm, referenced in the premise
# Also, it talks about the amount of food each horse is fed per day and total horse food per day, which are same in the premise and hypothesis
if ratio_hypothesis >= ratio_premise:
    # Check if the ratio of sheep to horses in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # The premise gives an exact value of the ratio
    # Any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
