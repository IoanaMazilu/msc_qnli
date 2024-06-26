england_france_premise = 0
england_italy_premise = 6
france_italy_premise = 11

# the hypothesis refers to the number of members who traveled to both England and France, and the number of members who traveled to both Italy and France
if england_france_premise == 0 and england_italy_premise!= 6 and france_italy_premise!= 11:
    # check if the hypothesis values contradict the number of members who traveled to both England and France reported in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of members who traveled to both England and France
    # any number of members who traveled to both England and France consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
