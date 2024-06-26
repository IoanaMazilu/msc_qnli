kittens_premise = 8.0
given_kittens_premise = 2.0
kittens_hypothesis = 4.0

# the hypothesis refers to the number of kittens, which are also mentioned in the premise
# compute the current number of kittens in the premise
current_kittens_premise = kittens_premise - given_kittens_premise
if kittens_hypothesis!= current_kittens_premise:
    # check if the number of kittens in the hypothesis contradicts the number of kittens from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
