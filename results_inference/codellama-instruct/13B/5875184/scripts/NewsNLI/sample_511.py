# define variables for the entities in the premise
rebel_group_leader = "Suarez"
rebel_group_member = "Cano"
military_experience_leader = 10
military_experience_member = 5
time_served_leader = 5
time_served_member = 2

# define variables for the entities in the hypothesis
hypothesis_leader = "Suarez"
hypothesis_member = "Cano"

# check if the leader in the hypothesis is the same as the leader in the premise
if hypothesis_leader == rebel_group_leader:
    # check if the leader in the hypothesis has more military experience and time served than the member in the premise
    if military_experience_leader > military_experience_member and time_served_leader > time_served_member:
        # if the leader in the hypothesis has more military experience and time served than the member in the premise, we can infer entailment
        label = "entailment"
    else:
        # if the leader in the hypothesis does not have more military experience and time served than the member in the premise, we can infer contradiction
        label = "contradiction"
else:
    # if the leader in the hypothesis is not the same as the leader in the premise, we can infer neutral
    label = "neutral"

print(label)
