bought_cookies_premise = 16.0
eaten_cookies_premise = 12.0
left_cookies_hypothesis = 0.0

# the hypothesis refers to the number of cookie packs left, which can be inferred from the premise
# compute the number of cookie packs left in the premise
left_cookies_premise = bought_cookies_premise - eaten_cookies_premise
if left_cookies_hypothesis != left_cookies_premise:
    # check if the number of cookie packs left in the hypothesis contradicts the number of cookie packs left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
