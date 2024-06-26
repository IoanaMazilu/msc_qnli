shoes_premise = 27
shoes_hypothesis = 27

# the hypothesis refers to the number of pairs of shoes Marcella has, mentioned in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the hypothesis value contradicts the exact number of'shoes_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
