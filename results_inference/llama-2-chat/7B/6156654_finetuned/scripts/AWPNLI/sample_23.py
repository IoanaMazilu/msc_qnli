joan_cats_premise = 8.0
given_cats_premise = 2.0
current_cats_hypothesis = 4.0

# the hypothesis refers to the number of kittens Joan has now, which is also mentioned in the premise
# compute the current number of kittens Joan has now, according to the premise
current_cats_premise = joan_cats_premise - given_cats_premise

if current_cats_hypothesis!= current_cats_premise:
    # check if the number of kittens Joan has now, according to the hypothesis, contradicts the number of kittens Joan has now, according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
