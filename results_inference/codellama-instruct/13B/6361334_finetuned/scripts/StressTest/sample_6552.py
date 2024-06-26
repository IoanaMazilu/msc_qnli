members_england_premise = 30
members_england_hypothesis = 70
members_france_premise = 26
members_france_hypothesis = 26
members_italy_premise = 32
members_italy_hypothesis = 32

# the hypothesis refers to the number of members of a certain club that traveled to England
if members_england_hypothesis >= members_england_premise:
    # check if the hypothesis value contradicts the number of members that traveled to England in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of members that traveled to England
    # any number of members less than'members_england_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
