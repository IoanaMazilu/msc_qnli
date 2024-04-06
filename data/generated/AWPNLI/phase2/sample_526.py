# Premise: Lucy went to the grocery store and she bought 16.0 packs of cookies and ate 12.0 packs of them.
# Hypothesis: She has 4.0 packs of cookies left.
# Golden Label: entailment

bought_cookies_premise = 16.0
ate_cookies_premise = 12.0
left_cookies_hypothesis = 4.0

# the hypothesis refers to the number of packs of cookies left, which are also referenced in the premise
# compute the remaining number of packs of cookies in the premise
left_cookies_premise = bought_cookies_premise - ate_cookies_premise
if left_cookies_hypothesis != left_cookies_premise:
    # check if the number of packs of cookies left in the hypothesis contradicts the number of packs of cookies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

