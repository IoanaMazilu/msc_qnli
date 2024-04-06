# Premise: Cindy’s mom baked 41.0 cookies and Paul’s dad ate 38.0.
# Hypothesis: 0.0 cookies are left.
# Golden Label: contradiction

baked_cookies_premise = 41.0
eaten_cookies_premise = 38.0
left_cookies_hypothesis = 0.0

# the hypothesis refers to the number of cookies left, which is related to the number of cookies baked and eaten in the premise
# compute the number of cookies left in the premise
left_cookies_premise = baked_cookies_premise - eaten_cookies_premise
if left_cookies_hypothesis != left_cookies_premise:
    # check if the number of cookies left in the hypothesis contradicts the number of cookies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

