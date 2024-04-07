# Premise: Each of the 59 members in Lourdes school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Hypothesis: Each of the more than 59 members in Lourdes school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Golden Label: contradiction

members_premise = 59
members_hypothesis = 60

# the hypothesis talks about the number of members in Lourdes school class, which is also mentioned in the premise
if members_hypothesis <= members_premise:
    # check if the number of members in the hypothesis contradicts the number of members mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of members
    # any number of members greater than 'members_premise' cannot be explicitly entailed from the premise, but is not in contradiction
    label = "neutral"

print(label)

