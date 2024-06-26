math_score_premise = 76
math_score_hypothesis = 46
sci_score_premise = 65
sci_score_hypothesis = 65
soc_stud_score_premise = 82
soc_stud_score_hypothesis = 82
eng_score_premise = 67
eng_score_hypothesis = 75
bio_score_premise = 75

# check if the hypothesis values contradict the premise values
if math_score_hypothesis < math_score_premise:
    label = "contradiction"
elif sci_score_hypothesis < sci_score_premise:
    label = "contradiction"
elif soc_stud_score_hypothesis < soc_stud_score_premise:
    label = "contradiction"
elif eng_score_hypothesis < eng_score_premise:
    label = "contradiction"
elif bio_score_hypothesis < bio_score_premise:
    label = "contradiction"
else:
    # if all hypothesis values are consistent with the premise values, we can infer entailment
    label = "entailment"

print(label)
