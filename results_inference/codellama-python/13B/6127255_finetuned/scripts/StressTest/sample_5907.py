math_marks_premise = 76
science_marks_premise = 65
social_studies_marks_premise = 82
english_marks_premise = 67
biology_marks_premise = 75

math_marks_hypothesis = 46
science_marks_hypothesis = 65
social_studies_marks_hypothesis = 82
english_marks_hypothesis = 67
biology_marks_hypothesis = 75

# the hypothesis refers to the marks scored by Shekar in different subjects mentioned in the premise
if math_marks_premise <= math_marks_hypothesis or science_marks_premise < science_marks_hypothesis or social_studies_marks_premise < social_studies_marks_hypothesis or english_marks_premise < english_marks_hypothesis or biology_marks_premise < biology_marks_hypothesis:
    # check if the marks in any subject in the hypothesis contradict the marks in the same subject in the premise
    label = "contradiction"
elif math_marks_premise > math_marks_hypothesis and science_marks_premise == science_marks_hypothesis and social_studies_marks_premise == social_studies_marks_hypothesis and english_marks_premise == english_marks_hypothesis and biology_marks_premise == biology_marks_hypothesis:
    # check if the marks in any subject in the hypothesis are more than the marks in the same subject in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
