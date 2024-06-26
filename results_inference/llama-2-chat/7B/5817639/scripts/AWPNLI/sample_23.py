kittens_premise = float(8.0)
kittens_hypothesis = float(4.0)

# compare the number of kittens in the premise and hypothesis
if kittens_premise == kittens_hypothesis:
    # if the number of kittens in the hypothesis is equal to the number of kittens in the premise, we can infer entailment
    label = "entailment"
elif kittens_hypothesis < kittens_premise:
    # if the number of kittens in the hypothesis is less than the number of kittens in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
