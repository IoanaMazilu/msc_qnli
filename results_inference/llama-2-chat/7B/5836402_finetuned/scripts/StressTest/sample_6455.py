english_score_premise = 66
mathematics_score_premise = 60
chemistry_score_premise = 72
biology_score_premise = 77
french_score_premise = 55
physics_score_premise = 85

english_score_hypothesis = 66
mathematics_score_hypothesis = 60
chemistry_score_hypothesis = 72
biology_score_hypothesis = 77
french_score_hypothesis = 55
physics_score_hypothesis = 85

# the hypothesis refers to the scores of the examination mentioned in the premise
if english_score_hypothesis >= english_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'english_score_premise'
    label = "contradiction"
elif mathematics_score_hypothesis >= mathematics_score_premise:
    # check if the hypothesis value contradicts the estimate of less than'mathematics_score_premise'
    label = "contradiction"
elif chemistry_score_hypothesis >= chemistry_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'chemistry_score_premise'
    label = "contradiction"
elif biology_score_hypothesis >= biology_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'biology_score_premise'
    label = "contradiction"
elif french_score_hypothesis >= french_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'french_score_premise'
    label = "contradiction"
elif physics_score_hypothesis >= physics_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'physics_score_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
