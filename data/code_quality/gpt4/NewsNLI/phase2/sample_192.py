ships_sank_premise = 50
ships_sank_hypothesis = 50

# the hypothesis mentions the number of American ships sank in the Gulf, which is also referenced in the premise
if ships_sank_hypothesis != ships_sank_premise:
    # check if the number of ships sank in the hypothesis contradicts the number of ships sank in the premise
    label = "contradiction"
else:
    # if the number of ships sank in the hypothesis does not contradict the number of ships sank in the premise, we can infer entailment
    label = "entailment"

print(label)
