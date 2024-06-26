cookies_baked_premise = 41.0
cookies_eaten_premise = 38.0
cookies_left_hypothesis = 0.0

# the hypothesis refers to the number of cookies left, which is also mentioned in the premise
# compute the number of cookies left in the premise
cookies_left_premise = cookies_baked_premise - cookies_eaten_premise
if cookies_left_hypothesis!= cookies_left_premise:
    # check if the number of cookies left in the hypothesis contradicts the number of cookies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
