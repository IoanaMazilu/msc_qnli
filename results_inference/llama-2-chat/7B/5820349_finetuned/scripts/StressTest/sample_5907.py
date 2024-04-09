math_marks_premise = 76
math_marks_hypothesis = 46
science_marks_premise = 65
science_marks_hypothesis = 65
social_studies_marks_premise = 82
social_studies_marks_hypothesis = 82
english_marks_premise = 67
english_marks_hypothesis = 67
biology_marks_premise = 75
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in each subject mentioned in the premise
if math_marks_hypothesis >= math_marks_premise:
    # check if the estimate of'math_marks_hypothesis' contradicts the mark in Mathematics in the premise
    label = "contradiction"
elif science_marks_hypothesis!= science_marks_premise:
    # check if the mark in Science in the hypothesis contradicts the mark in Science reported in the premise
    label = "contradiction"
elif social_studies_marks_hypothesis!= social_studies_marks_premise:
    # check if the mark in Social studies in the hypothesis contradicts the mark in Social studies reported in the premise
    label = "contradiction"
elif english_marks_hypothesis!= english_marks_premise:
    # check if the mark in English in the hypothesis contradicts the mark in English reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis!= biology_marks_premise:
    # check if the mark in Biology in the hypothesis contradicts the mark in Biology reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
