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

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
if math_marks_premise <= math_marks_hypothesis:
    # check if the estimate of'math_marks_hypothesis' contradicts the marks scored in Mathematics in the premise
    label = "contradiction"
elif science_marks_premise!= science_marks_hypothesis:
    # check if the marks scored in Science in the hypothesis contradicts the marks scored in Science in the premise
    label = "contradiction"
elif social_studies_marks_premise!= social_studies_marks_hypothesis:
    # check if the marks scored in Social studies in the hypothesis contradicts the marks scored in Social studies in the premise
    label = "contradiction"
elif english_marks_premise!= english_marks_hypothesis:
    # check if the marks scored in English in the hypothesis contradicts the marks scored in English in the premise
    label = "contradiction"
elif biology_marks_premise!= biology_marks_hypothesis:
    # check if the marks scored in Biology in the hypothesis contradicts the marks scored in Biology in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
