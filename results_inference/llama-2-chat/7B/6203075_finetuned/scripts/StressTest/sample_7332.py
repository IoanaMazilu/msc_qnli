samsung_phone_users_premise = 75
samsung_phone_users_hypothesis = 25
iphone_users_premise = 70
iphone_users_hypothesis = 70

# the hypothesis refers to the percentage of Samsung phone users and iPhone users in the same company
if samsung_phone_users_premise <= samsung_phone_users_hypothesis:
    # check if the estimate of'samsung_phone_users_hypothesis' contradicts the percentage of Samsung phone users in the premise
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
