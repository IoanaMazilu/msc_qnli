shoes_premise = 25
shoes_hypothesis = 25

# the hypothesis refers to the number of shoes Marcella has, mentioned in the premise
if shoes_premise >= shoes_hypothesis:
    # check if the number of shoes in the premise contradicts the hypothesis of less than'shoes_hypothesis'
    label = "contradiction"
else:
    # if the number of shoes in the premise is less than the one in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
