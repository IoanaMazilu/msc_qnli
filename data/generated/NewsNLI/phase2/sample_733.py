# Premise: Change.org, based in San Francisco, California, says it has 35 million users in 196 countries.
# Hypothesis: The website says it has more than 35 million users.
# Golden Label: neutral

users_premise = 35000000
users_hypothesis = 35000000

# the hypothesis mentions the number of users, which is also referenced in the premise
if users_hypothesis > users_premise:
    # check if the number of users in the hypothesis contradicts the number of users in the premise
    label = "contradiction"
else:
    # if the number of users in the hypothesis does not contradict the number of users in the premise, we can infer entailment
    label = "entailment"

print(label)

