shoes_premise = 25
shoes_hypothesis = 25

# the hypothesis refers to the number of shoes Marcella has, which is also mentioned in the premise
if shoes_hypothesis >= shoes_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
