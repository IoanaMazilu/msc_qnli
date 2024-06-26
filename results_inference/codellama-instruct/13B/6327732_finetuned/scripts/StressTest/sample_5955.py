members_club_premise = 26
members_club_hypothesis = 56
members_france_premise = 26
members_france_hypothesis = 26
members_italy_premise = 32
members_italy_hypothesis = 32

# the hypothesis talks about the number of members of a certain club that traveled to England
if members_club_hypothesis >= members_club_premise:
    # check if the hypothesis value contradicts the number of members of the club that traveled to England in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of members that traveled to England
    # any number of members less than'members_club_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
