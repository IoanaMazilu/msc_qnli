discount_premise = 20
discount_hypothesis = 50
paid_each = 4

# the hypothesis talks about the discount Saren negotiated, which is also mentioned in the premise
if discount_hypothesis!= discount_premise:
    # check if the discount in the hypothesis contradicts the discount in the premise
    label = "contradiction"
elif paid_each!= 4:
    # check if the number of dollars each paid in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
