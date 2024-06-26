# number of chairs needed for seating all people
chairs_premise = 5
chairs_hypothesis = 4

# the hypothesis talks about the number of chairs needed, which is also referenced in the premise
if chairs_hypothesis != chairs_premise:
    # check if the number of chairs in the hypothesis contradicts the number of chairs in the premise
    label = "contradiction"
else:
    # if the number of chairs in the hypothesis does not contradict the number of chairs in the premise, we can infer entailment
    label = "entailment"

print(label)
