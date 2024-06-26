guests_premise = 37
guests_hypothesis = 37

# the hypothesis talks about the number of guests, which is also referenced in the premise
# check if the number of guests in the hypothesis contradicts the number of guests in the premise
if guests_hypothesis == guests_premise:
    # if the number of guests in the hypothesis does not contradict the number of guests in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of guests in the hypothesis contradicts the number of guests in the premise, we can infer contradiction
    label = "contradiction"

print(label)
