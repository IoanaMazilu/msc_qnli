england_france_premise = 6
england_italy_premise = 0
france_italy_premise = 11

england_france_hypothesis = 8
england_italy_hypothesis = 0
france_italy_hypothesis = 11

# the hypothesis refers to the number of members who traveled to England and France, and to France and Italy
if england_france_hypothesis <= england_france_premise:
    # check if the hypothesis value contradicts the number of members who traveled to England and France in the premise
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise:
    # check if the number of members who traveled to England and Italy in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
