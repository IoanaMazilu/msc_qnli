english_score_premise = 66
mathematics_score_premise = 60
chemistry_score_premise = 72
biology_score_premise = 77
french_score_premise = 55
physics_score_premise = 85

average_score_premise = 0

for score in [english_score_premise, mathematics_score_premise, chemistry_score_premise, biology_score_premise, french_score_premise, physics_score_premise]:
    average_score_premise += score

average_score_hypothesis = 0

for score in [english_score_premise, mathematics_score_premise, chemistry_score_premise, biology_score_premise, french_score_premise, physics_score_premise]:
    average_score_hypothesis += score

# the hypothesis refers to the average score of Andrea, which is also computed in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score from the premise
    label = "contradiction"
else:
    # if the average score in the hypothesis does not contradict the average score from the premise, we can infer entailment
    label = "entailment"

print(label)
