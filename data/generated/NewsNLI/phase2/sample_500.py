# Premise: In Spain's La Liga, second half penalties from Mali international Freddy Kanoute and Spanish striker Alvaro Negredo helped Sevilla to a 3-1 home win over strugglers Real Zaragoza.
# Hypothesis: Sevilla beat Real Zaragoza 3-1 to go fifth in Spain's La Liga.
# Golden Label: neutral

sevilla_score_premise = 3
zaragoza_score_premise = 1
sevilla_score_hypothesis = 3
zaragoza_score_hypothesis = 1

# the hypothesis mentions the score between Sevilla and Real Zaragoza, which is also referenced in the premise
# however, the hypothesis introduces a new information about Sevilla's position in La Liga, which cannot be entailed from the premise
if sevilla_score_hypothesis != sevilla_score_premise:
    # check if the sevilla score in the hypothesis contradicts the sevilla score reported in the premise
    label = "contradiction"
elif zaragoza_score_hypothesis != zaragoza_score_premise:
    # check if the zaragoza score from the hypothesis contradicts the zaragoza score in the premise
    label = "contradiction"
else:
    # if the hypothesis score values do not contradict the premise score values, we cannot infer entailment due to additional information
    label = "neutral"

print(label)

