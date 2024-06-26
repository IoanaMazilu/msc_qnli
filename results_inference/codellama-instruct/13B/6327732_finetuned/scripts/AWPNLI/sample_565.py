cookies_baked_premise = 41.0
cookies_ate_premise = 38.0
cookies_left_hypothesis = 0.0

# the hypothesis refers to the number of cookies left, which are also mentioned in the premise
# compute the total number of cookies baked and ate
total_cookies_premise = cookies_baked_premise + cookies_ate_premise
if cookies_left_hypothesis!= total_cookies_premise:
    # check if the number of cookies left in the hypothesis contradicts the number of cookies baked and ate from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
