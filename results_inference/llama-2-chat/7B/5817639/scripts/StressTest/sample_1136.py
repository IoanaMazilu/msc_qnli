shirts_premise = 1
shirts_hypothesis = 5
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the number of shirts, jeans, and sneakers in an outfit
if shirts_hypothesis <= shirts_premise:
    # check if the hypothesis value contradicts the estimate of'shirts_premise'
    label = "contradiction"
elif jeans_hypothesis!= jeans_premise or sneakers_hypothesis!= sneakers_premise:
    # check if the number of jeans or sneakers in the hypothesis contradicts the number of jeans or sneakers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
