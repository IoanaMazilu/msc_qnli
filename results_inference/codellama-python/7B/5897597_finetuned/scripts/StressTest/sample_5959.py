england_france_premise = 8
england_france_hypothesis = 6
england_italy_premise = 0
england_italy_hypothesis = 0
france_italy_premise = 11
france_italy_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to England and France, England and Italy, and France and Italy, as mentioned in the premise
if england_france_hypothesis >= england_france_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_france_premise'
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise or france_italy_hypothesis!= france_italy_premise:
    # check if the number of club members who traveled to England and Italy or France and Italy in the hypothesis contradicts the number of such members reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of club members who traveled to England and France
    # any number of such members less than 'england_france_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
