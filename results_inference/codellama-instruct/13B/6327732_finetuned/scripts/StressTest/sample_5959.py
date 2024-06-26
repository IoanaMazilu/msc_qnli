members_club_premise = 8
members_club_hypothesis = 6

# the hypothesis refers to the number of members of the club that traveled to both England and France
if members_club_hypothesis <= members_club_premise:
    # check if the hypothesis value contradicts the estimate of less than'members_club_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members of the club that traveled to both England and France
    # any number of members greater than'members_club_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
