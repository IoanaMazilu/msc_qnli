premise_amount = 450
hypothesis_amount = 750

# the hypothesis refers to the amount sold to George, mentioned in the premise
if premise_amount <= hypothesis_amount:
    # check if the estimate of 'hypothesis_amount' contradicts the amount sold to George in the premise
    label = "contradiction"
elif hypothesis_amount!= premise_amount:
    # check if the amount sold to George in the hypothesis contradicts the amount sold to George in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
