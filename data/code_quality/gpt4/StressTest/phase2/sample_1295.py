average_shirts_premise = 40
average_shirts_hypothesis = 10
shirts_purchased = 14

# the hypothesis refers to the average number of shirts with three people and the number of shirts they purchased
# first, we check if the initial average number of shirts contradicts the premise
if average_shirts_hypothesis != average_shirts_premise:
    label = "contradiction"
else:
    # then, we calculate the new average number of shirts after the purchase
    new_average_shirts = (average_shirts_premise * 3 + shirts_purchased * 3) / 3
    # if the new average number of shirts is not equal to the initial average number, we have a contradiction
    if new_average_shirts != average_shirts_premise:
        label = "contradiction"
    else:
        # if the new average number of shirts is equal to the initial average number, we have entailment
        label = "entailment"

print(label)
