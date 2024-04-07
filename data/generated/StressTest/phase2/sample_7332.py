# Premise: In ABC limited, 75% are using Samsung phone at the same time 70% using i phone ; If in the same company 85% are using Samsung phone then, what is the percentage of i phone user?
# Hypothesis: In ABC limited, more than 25% are using Samsung phone at the same time 70% using i phone ; If in the same company 85% are using Samsung phone then, what is the percentage of i phone user?
# Golden Label: entailment

samsung_users_premise = 75
samsung_users_hypothesis = 25
iphone_users_premise = 70
iphone_users_hypothesis = 70
alternative_samsung_users_premise = 85
alternative_samsung_users_hypothesis = 85

# the hypothesis talks about the percentage of Samsung and iPhone users in the same company, referenced also in the premise
if samsung_users_hypothesis > samsung_users_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif iphone_users_hypothesis != iphone_users_premise:
    # check if the number of iPhone users in the hypothesis contradicts the number of iPhone users reported in the premise
    label = "contradiction"
elif alternative_samsung_users_hypothesis != alternative_samsung_users_premise:
    # check if the alternative scenario of Samsung users in the hypothesis contradicts the alternative scenario of Samsung users in the premise
    label = "contradiction"
else:
    # if none of the hypothesis values contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

