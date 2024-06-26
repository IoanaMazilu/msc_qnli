shirts_outfit_premise = 1
jeans_outfit_premise = 1
sneakers_outfit_premise = 1

shirts_outfit_hypothesis = 5
jeans_outfit_hypothesis = 1
sneakers_outfit_hypothesis = 1

# the hypothesis gives an estimate for the number of shirts, referenced also in the premise
if shirts_outfit_hypothesis <= shirts_outfit_premise:
    # check if the hypothesis value contradicts the number of shirts reported in the premise
    label = "contradiction"
elif jeans_outfit_hypothesis!= jeans_outfit_premise or sneakers_outfit_hypothesis!= sneakers_outfit_premise:
    # check if the number of jeans or sneakers in the hypothesis contradicts the number of jeans or sneakers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
