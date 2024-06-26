car_owners_premise = 18
car_owners_hypothesis = 48

# the hypothesis refers to the percentage of students owning cars at Morse, mentioned in the premise
if car_owners_hypothesis <= car_owners_premise:
    # check if the hypothesis value contradicts the percentage of 'car_owners_premise'
    label = "contradiction"
elif car_owners_hypothesis > car_owners_premise:
    # if the hypothesis value is greater than 'car_owners_premise', it can be inferred from the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to 'car_owners_premise', it does not contradict the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
