chairs_premise = 6
chairs_hypothesis = 4

# the hypothesis refers to the number of chairs mentioned in the premise
if chairs_hypothesis >= chairs_premise:
    # check if the number of chairs in the hypothesis contradicts the number of chairs in the premise
    label = "contradiction"
else:
    # if the number of chairs in the hypothesis does not contradict the number of chairs in the premise, we have entailment
    label = "entailment"

print(label)
