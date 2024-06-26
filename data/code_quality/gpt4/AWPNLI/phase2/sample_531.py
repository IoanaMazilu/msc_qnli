candies_linda_premise = 34.0
candies_given_premise = 28.0
candies_left_hypothesis = 2.0

# the hypothesis refers to the number of candies left with Linda, which is also mentioned in the premise
# compute the number of candies left with Linda in the premise
candies_left_premise = candies_linda_premise - candies_given_premise
if candies_left_hypothesis != candies_left_premise:
    # check if the number of candies left in the hypothesis contradicts the number of candies left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
