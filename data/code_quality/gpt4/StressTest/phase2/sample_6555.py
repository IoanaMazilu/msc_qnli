england_france_premise = 0
england_france_hypothesis = 0
england_italy_premise = 6
england_italy_hypothesis = 7
france_italy_premise = 11
france_italy_hypothesis = 11

# the hypothesis refers to the same travels done by the club members, mentioned in the premise
if england_france_hypothesis != england_france_premise:
    # check if the hypothesis value contradicts the one from the premise
    label = "contradiction"
elif england_italy_premise >= england_italy_hypothesis:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif france_italy_hypothesis != france_italy_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
