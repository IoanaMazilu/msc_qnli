shoes_premise = 65
shoes_hypothesis = 25

# the hypothesis refers to the number of shoes Marcella has, which is also mentioned in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the number of shoes in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of shoes in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
