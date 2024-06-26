members_england_france_premise = 6
members_england_france_hypothesis = 8
members_italy_premise = 11
members_italy_hypothesis = 11

# the hypothesis refers to the number of members who traveled to both England and France, which is also mentioned in the premise
if members_england_france_hypothesis >= members_england_france_premise:
    # check if the hypothesis value contradicts the number of members who traveled to both England and France in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to both England and France
    # any number of members less than'members_england_france_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
