# Premise: Schalke moved up to third place with a 2-0 win at home to Hannover, who were mourning the suicide of Germany goalkeeper Robert Enke.
# Hypothesis: Schalke move into third place after 2-0 win over Hannover, who are mourning Robert Enke.
# Golden Label: entailment

schalke_position_premise = 3
schalke_position_hypothesis = 3
schalke_score_premise = 2
schalke_score_hypothesis = 2

# the hypothesis mentions the new position of Schalke and the score of the match, which are also mentioned in the premise
if schalke_position_hypothesis != schalke_position_premise:
    # check if the Schalke's position in the hypothesis contradicts Schalke's position reported in the premise
    label = "contradiction"
elif schalke_score_hypothesis != schalke_score_premise:
    # check if the Schalke's score from the hypothesis contradicts Schalke's score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

