product_age_premise = 32
product_age_hypothesis = 62

# the hypothesis talks about the product of Diana's age and a third of Rashid's age
if product_age_hypothesis != product_age_premise:
    # check if the product of ages in the hypothesis contradicts the product of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
