baked_cookies_premise = 41.0
ate_cookies_premise = 38.0
left_cookies_hypothesis = 0.0

# the hypothesis refers to the number of cookies left, which is not mentioned in the premise
# compute the total number of cookies in the premise
total_cookies_premise = baked_cookies_premise + ate_cookies_premise
if left_cookies_hypothesis!= total_cookies_premise:
    # check if the number of cookies in the hypothesis contradicts the number of cookies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
