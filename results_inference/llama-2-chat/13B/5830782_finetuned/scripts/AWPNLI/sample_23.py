initial_kittens_premise = 8.0
given_kittens_premise = 2.0
remaining_kittens_hypothesis = 4.0

# the hypothesis refers to the number of remaining kittens, which is also mentioned in the premise
# compute the remaining number of kittens in the premise
remaining_kittens_premise = initial_kittens_premise - given_kittens_premise
if remaining_kittens_hypothesis!= remaining_kittens_premise:
    # check if the number of remaining kittens in the hypothesis contradicts the number of remaining kittens from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
