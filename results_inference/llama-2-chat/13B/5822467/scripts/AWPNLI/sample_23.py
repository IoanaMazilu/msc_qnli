kittens_premise = 8.0
kittens_given_premise = 2.0
kittens_hypothesis = 4.0

# compute the total number of kittens in the premise
total_kittens_premise = kittens_premise + kittens_given_premise

if kittens_hypothesis < total_kittens_premise:
    # check if the number of kittens in the hypothesis contradicts the number of kittens from the premise
    label = "contradiction"
elif kittens_hypothesis > total_kittens_premise:
    # check if the number of kittens in the hypothesis entails the number of kittens from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
