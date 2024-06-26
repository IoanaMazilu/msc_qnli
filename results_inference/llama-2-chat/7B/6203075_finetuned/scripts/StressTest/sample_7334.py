samsung_users_premise = 75
samsung_users_hypothesis = 85
iphone_users_premise = 70
iphone_users_hypothesis = 70

# the hypothesis talks about the percentage of Samsung and iPhone users in the same company,
# which is also referenced in the premise
if samsung_users_hypothesis <= samsung_users_premise:
    # check if the hypothesis value contradicts the premise value of Samsung users
    label = "contradiction"
elif iphone_users_hypothesis!= iphone_users_premise:
    # check if the hypothesis value contradicts the premise value of iPhone users
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
