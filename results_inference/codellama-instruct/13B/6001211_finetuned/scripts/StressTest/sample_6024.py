percentage_given_back_premise = 4
percentage_given_back_hypothesis = 6

# the hypothesis refers to the percentage given back each month by Dana, mentioned also in the premise
if percentage_given_back_hypothesis < percentage_given_back_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
