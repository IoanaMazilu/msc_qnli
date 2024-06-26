math_marks_premise = 46
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 95

math_marks_hypothesis = 76
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 95

# the hypothesis talks about the marks scored in different subjects, referenced also in the premise
if math_marks_hypothesis <= math_marks_premise or science_marks_hypothesis != science_marks_premise or social_studies_marks_hypothesis != social_studies_marks_premise or english_marks_hypothesis != english_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'math_marks_premise' or if any of the other subject scores differ
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
