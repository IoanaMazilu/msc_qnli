car_owners_premise = 15
car_owners_hypothesis = 15

# the hypothesis refers to the percentage of Morse students who own cars mentioned in the premise
if car_owners_hypothesis > car_owners_premise:
    # check if the hypothesis percentage contradicts the percentage from the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
