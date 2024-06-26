members_premise = 59
members_hypothesis = 59
min_clubs_premise = 1
max_clubs_premise = 3
min_clubs_hypothesis = 1
max_clubs_hypothesis = 3

# the hypothesis refers to the number of members and the number of clubs they are required to sign up for, mentioned in the premise
if members_hypothesis <= members_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif min_clubs_hypothesis!= min_clubs_premise or max_clubs_hypothesis!= max_clubs_premise:
    # check if the number of clubs in the hypothesis contradicts the number of clubs reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members
    # any number of members greater than'members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)