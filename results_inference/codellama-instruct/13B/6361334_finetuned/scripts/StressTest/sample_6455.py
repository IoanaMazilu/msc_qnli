marks_english_premise = 66
marks_mathematics_premise = 60
marks_chemistry_premise = 72
marks_biology_premise = 77
marks_french_premise = 55
marks_physics_premise = 85

marks_english_hypothesis = 66
marks_mathematics_hypothesis = 60
marks_chemistry_hypothesis = 72
marks_biology_hypothesis = 77
marks_french_hypothesis = 55
marks_physics_hypothesis = 85

# the hypothesis refers to the scores in an examination, which are also mentioned in the premise
if marks_english_hypothesis < marks_english_premise:
    # check if the hypothesis value contradicts the score in English in the premise
    label = "contradiction"
elif marks_mathematics_hypothesis < marks_mathematics_premise:
    # check if the hypothesis value contradicts the score in Mathematics in the premise
    label = "contradiction"
elif marks_chemistry_hypothesis < marks_chemistry_premise:
    # check if the hypothesis value contradicts the score in Chemistry in the premise
    label = "contradiction"
elif marks_biology_hypothesis < marks_biology_premise:
    # check if the hypothesis value contradicts the score in Biology in the premise
    label = "contradiction"
elif marks_french_hypothesis < marks_french_premise:
    # check if the hypothesis value contradicts the score in French Language in the premise
    label = "contradiction"
elif marks_physics_hypothesis < marks_physics_premise:
    # check if the hypothesis value contradicts the score in Physics in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
