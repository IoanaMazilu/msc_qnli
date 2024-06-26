supermarkets_diff_premise = 74
supermarkets_diff_hypothesis = 14

# the hypothesis refers to the difference in the number of FGH supermarkets between the US and Canada
if supermarkets_diff_hypothesis >= supermarkets_diff_premise:
    # check if the hypothesis value contradicts the estimate of less than 'supermarkets_diff_premise' in the premise
    label = "contradiction"
elif supermarkets_diff_hypothesis < supermarkets_diff_premise:
    # the premise gives only an estimate for the difference in the number of supermarkets
    # a number less than 'supermarkets_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
