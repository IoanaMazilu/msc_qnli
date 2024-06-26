cars_purchased_premise = 3
cars_purchased_hypothesis = 7

# the hypothesis refers to the number of cars purchased by Sheik Abdullah mentioned in the premise
if cars_purchased_premise > cars_purchased_hypothesis:
    # check if the number of 'cars_purchased_premise' contradicts the estimate of less than 'cars_purchased_hypothesis' 
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
