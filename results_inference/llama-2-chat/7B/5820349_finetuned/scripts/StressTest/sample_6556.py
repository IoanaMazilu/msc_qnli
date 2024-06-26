england_france_premise = 0
england_france_hypothesis = 0
england_italy_premise = 7
england_italy_hypothesis = 6
france_italy_premise = 11
france_italy_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to England, France, Italy, England and Italy, and France and Italy
if england_france_hypothesis > england_france_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_france_premise'
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise:
    # check if the number of club members who traveled to England and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif france_italy_hypothesis!= france_italy_premise:
    # check if the number of club members who traveled to France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only estimates for the number of club members who traveled to England, France, and Italy
    # any number of club members less than 'england_france_premise' and equal to 'england_italy_premise' and 'france_italy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
