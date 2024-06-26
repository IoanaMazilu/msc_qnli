members_england_france_premise = 8
members_england_france_hypothesis = 6
members_england_italy_premise = 0
members_england_italy_hypothesis = 0
members_france_italy_premise = 11
members_france_italy_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to various countries as mentioned in the premise
if members_england_france_hypothesis >= members_england_france_premise:
    # check if the number of members who traveled to England and France in the hypothesis contradicts the premise
    label = "contradiction"
elif members_england_italy_hypothesis!= members_england_italy_premise:
    # check if the number of members who traveled to England and Italy in the hypothesis contradicts the premise
    label = "contradiction"
elif members_france_italy_hypothesis!= members_france_italy_premise:
    # check if the number of members who traveled to France and Italy in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to England and France
    # any number of members less than'members_england_france_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
