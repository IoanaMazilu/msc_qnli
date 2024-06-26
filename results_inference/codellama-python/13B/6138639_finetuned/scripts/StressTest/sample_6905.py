total_paid_premise = 160
total_paid_hypothesis = 760

# the hypothesis talks about the total amount paid by Rahul, which is also mentioned in the premise
if total_paid_hypothesis!= total_paid_premise:
    # check if the total amount paid in the hypothesis contradicts the total amount paid in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
