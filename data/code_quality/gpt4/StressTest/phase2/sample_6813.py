car_owners_premise = 18
car_owners_hypothesis = 48

# the hypothesis refers to the percentage of students with cars mentioned in the premise
if car_owners_hypothesis < car_owners_premise:
    # check if the estimate of 'car_owners_hypothesis' contradicts the percentage of car owners in the premise
    label = "contradiction"
elif car_owners_hypothesis == car_owners_premise:
    # if the hypothesis and premise percentages are the same, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis percentage does not contradict the premise one, but it's not the same either, we infer neutrality
    label = "neutral"

print(label)
