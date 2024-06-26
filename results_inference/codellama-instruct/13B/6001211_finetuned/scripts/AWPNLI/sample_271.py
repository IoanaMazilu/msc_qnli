scored_candy_premise = 47.0
ate_candy_premise = 25.0
received_candy_premise = 40.0
total_candy_hypothesis = 65.0

# the hypothesis refers to the total number of candies Faye has, which is also mentioned in the premise
# compute the total number of candies Faye has in the premise
total_candy_premise = scored_candy_premise - ate_candy_premise + received_candy_premise
if total_candy_hypothesis!= total_candy_premise:
    # check if the total number of candies in the hypothesis contradicts the total number of candies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
