samsung_users_premise = 75
samsung_users_hypothesis = 25
iphone_users_premise = 70
iphone_users_hypothesis = 70
samsung_users_company = 85

# the hypothesis refers to the percentage of users using Samsung and iPhone phones in ABC limited and in the same company
if samsung_users_premise <= samsung_users_hypothesis:
    # check if the estimate of'samsung_users_hypothesis' contradicts the percentage of Samsung users in the premise
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users reported in the premise
    label = "contradiction"
elif samsung_users_company!= 85:
    # check if the percentage of Samsung users in the company contradicts the percentage of Samsung users in the company reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
