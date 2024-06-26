# scores in subjects for David as per premise
english_premise = 76
mathematics_premise = 65
physics_premise = 82
chemistry_premise = 67
biology_premise = 85

# scores in subjects for David as per hypothesis
english_hypothesis = 86
mathematics_hypothesis = 65
physics_hypothesis = 82
chemistry_hypothesis = 67
biology_hypothesis = 85

# comparison of scores in each subject
if english_hypothesis <= english_premise:
    # check if the hypothesis value contradicts the score of English in premise
    label = "contradiction"
elif mathematics_hypothesis != mathematics_premise:
    # check if the score of Mathematics in hypothesis contradicts the score of Mathematics in premise
    label = "contradiction"
elif physics_hypothesis != physics_premise:
    # check if the score of Physics in hypothesis contradicts the score of Physics in premise
    label = "contradiction"
elif chemistry_hypothesis != chemistry_premise:
    # check if the score of Chemistry in hypothesis contradicts the score of Chemistry in premise
    label = "contradiction"
elif biology_hypothesis != biology_premise:
    # check if the score of Biology in hypothesis contradicts the score of Biology in premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
