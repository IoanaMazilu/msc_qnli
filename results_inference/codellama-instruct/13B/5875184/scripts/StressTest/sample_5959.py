premise_england_france = 8
premise_england_italy = 0
premise_france_italy = 11

hypothesis_england_france = 6
hypothesis_england_italy = 0
hypothesis_france_italy = 11

# the hypothesis refers to the number of members who traveled to both England and France, which is less than the number of members who traveled to both France and Italy
if hypothesis_england_france <= premise_france_italy:
    # check if the hypothesis value contradicts the estimate of less than 'premise_england_france'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of members who traveled to both England and France
    # any number of members greater than 'premise_england_france' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
