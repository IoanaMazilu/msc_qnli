# Premise: Joan's cat had 8.0 kittens and she got 2.0 more from her friends.
# Hypothesis: She has 6.0 kittens now.
# Golden Label: contradiction

kittens_had_premise = 8.0
kittens_received_premise = 2.0
total_kittens_hypothesis = 6.0

# the hypothesis refers to the total number of kittens, which is also mentioned in the premise
# compute the total number of kittens in the premise
total_kittens_premise = kittens_had_premise + kittens_received_premise
if total_kittens_hypothesis != total_kittens_premise:
    # check if the number of kittens in the hypothesis contradicts the number of kittens from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

