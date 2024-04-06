# Premise: '' Historians say U-boats sank at least 50 American ships in the Gulf, one in the very mouth of the Mississippi River.
# Hypothesis: Nazis sank about 50 American ships in the Gulf during the war.
# Golden Label: entailment

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

