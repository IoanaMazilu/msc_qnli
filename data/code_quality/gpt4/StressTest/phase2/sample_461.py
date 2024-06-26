chairs_premise = 4
chairs_hypothesis = 6

# the hypothesis talks about the same seating arrangement as the premise but with a different number of chairs
if chairs_premise != chairs_hypothesis:
    # check if the number of chairs in the hypothesis contradicts the number of chairs mentioned in the premise
    label = "contradiction"
else:
    # if the number of chairs in the hypothesis does not contradict the number of chairs in the premise, we can infer entailment
    label = "entailment"

print(label)
