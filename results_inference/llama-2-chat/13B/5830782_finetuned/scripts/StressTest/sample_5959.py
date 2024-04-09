england_france_premise = 8
england_france_hypothesis = 6
england_italy_premise = 0
england_italy_hypothesis = 0
france_italy_premise = 11
france_italy_hypothesis = 11

# the hypothesis refers to the same travels to England, France, and Italy as mentioned in the premise
if england_france_hypothesis >= england_france_premise:
    # check if the number of members that traveled to England and France in the hypothesis contradicts the premise
    label = "contradiction"
elif england_italy_hypothesis!= england_italy_premise or france_italy_hypothesis!= france_italy_premise:
    # check if the number of members that traveled to England and Italy or France and Italy in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
