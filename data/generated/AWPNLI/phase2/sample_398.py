# Premise: Joan's cat had 8.0 kittens and she got 2.0 more from her friends.
# Hypothesis: She has 10.0 kittens now.
# Golden Label: entailment

born_kittens_premise = 8.0
received_kittens_premise = 2.0
total_kittens_hypothesis = 10.0

# the hypothesis refers to the total number of kittens, which are also mentioned in the premise
# compute the total number of kittens in the premise
total_kittens_premise = born_kittens_premise + received_kittens_premise
if total_kittens_hypothesis != total_kittens_premise:
    # check if the number of kittens in the hypothesis contradicts the number of kittens from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

