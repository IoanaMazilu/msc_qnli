premise_england = 26
premise_france = 26
premise_italy = 32

hypothesis_england = 26
hypothesis_france = 26
hypothesis_italy = 32

# the hypothesis refers to the number of members of a certain club that traveled to each country
if premise_england <= hypothesis_england and premise_france <= hypothesis_france and premise_italy <= hypothesis_italy:
    # check if the hypothesis values contradict the premise estimates
    label = "contradiction"
else:
    # the premise gives only estimates for the number of members that traveled to each country
    # any number of members greater than the premise estimates is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
