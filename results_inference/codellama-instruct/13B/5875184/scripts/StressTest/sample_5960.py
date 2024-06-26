premise_england_france = 6
premise_england_italy = 0
premise_france_italy = 11

hypothesis_england_france = 3
hypothesis_england_italy = 0
hypothesis_france_italy = 11

# the hypothesis refers to the number of members who traveled to both England and France, which is consistent with the premise
if hypothesis_england_france <= premise_england_france:
    # check if the hypothesis value contradicts the estimate of no members traveling to both England and Italy
    if hypothesis_england_italy!= premise_england_italy:
        label = "contradiction"
    # check if the hypothesis value contradicts the estimate of 11 members traveling to both France and Italy
    elif hypothesis_france_italy!= premise_france_italy:
        label = "contradiction"
    else:
        label = "entailment"
else:
    label = "neutral"

print(label)
