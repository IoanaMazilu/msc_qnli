# Premise: Each of the more than 19 members in Lourdes school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Hypothesis: Each of the 59 members in Lourdes school class is required to sign up for a minimum of one and a maximum of three academic clubs.
# Golden Label: neutral

members_premise = 19
members_hypothesis = 59
min_clubs_premise = 1
max_clubs_premise = 3
min_clubs_hypothesis = 1
max_clubs_hypothesis = 3

# the hypothesis talks about the number of members in Lourdes school class and the number of clubs they are required to sign up for, which are both referenced in the premise
if members_hypothesis <= members_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'members_premise'
    label = "contradiction"
elif min_clubs_hypothesis != min_clubs_premise or max_clubs_hypothesis != max_clubs_premise:
    # check if the required number of clubs in the hypothesis contradicts the required number of clubs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members
    # any number of members greater than 'members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

