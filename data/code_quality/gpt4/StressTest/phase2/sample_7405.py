lenses_premise = 7
lenses_hypothesis = 2

# the hypothesis refers to the number of lenses per telescope mentioned in the premise
if lenses_hypothesis >= lenses_premise:
    # check if the number of lenses in the hypothesis contradicts the estimate of less than 'lenses_premise'
    label = "contradiction"
else:
    # if the number of lenses in the hypothesis does not contradict the premise's estimate, we can infer entailment
    label = "entailment"

print(label)
