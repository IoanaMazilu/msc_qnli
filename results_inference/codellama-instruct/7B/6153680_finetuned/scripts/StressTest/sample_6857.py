iron_coins = 5
copper_coins = 5

# the hypothesis refers to the same situation as the premise
# the only difference is that the hypothesis mentions a sum of more than 1 ¢
sum_range_premise = range(1, 35)
sum_range_hypothesis = range(1, 35)

# the hypothesis refers to a sum range of more than 1 ¢
if sum_range_hypothesis[0]!= sum_range_premise[0]:
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same sum range
    # but the hypothesis mentions a sum range of more than 1 ¢
    # which is not entailed from the premise
    label = "neutral"

print(label)
