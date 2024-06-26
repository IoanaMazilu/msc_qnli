math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 55

math_marks_hypothesis = 86
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 55

# the hypothesis statement refers to the scores of Shekar in various subjects mentioned in the premise
if math_marks_premise >= math_marks_hypothesis or science_marks_premise >= science_marks_hypothesis or social_studies_marks_premise >= social_studies_marks_hypothesis or english_marks_premise >= english_marks_hypothesis or biology_marks_premise >= biology_marks_hypothesis:
    # check if any of the scores in the hypothesis contradict the scores mentioned in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
