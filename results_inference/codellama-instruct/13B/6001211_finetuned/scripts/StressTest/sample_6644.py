shoes_premise = 27
shoes_hypothesis = 27

# the hypothesis refers to the number of shoes Marcella has, which is also mentioned in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the hypothesis value contradicts the exact number of shoes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
