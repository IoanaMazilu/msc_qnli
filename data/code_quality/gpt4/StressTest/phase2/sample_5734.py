# defining the marks scored by Shekar as per the premise
marks_math_premise = 46
marks_science_premise = 65
marks_social_studies_premise = 82
marks_english_premise = 47
marks_biology_premise = 85

# defining the marks scored by Shekar as per the hypothesis
marks_math_hypothesis = 76
marks_science_hypothesis = 65
marks_social_studies_hypothesis = 82
marks_english_hypothesis = 47
marks_biology_hypothesis = 85

# comparing the marks in each subject as per the premise and hypothesis
if marks_math_hypothesis <= marks_math_premise:
    # check if the marks in Math as per the hypothesis contradict the premise
    label = "contradiction"
elif marks_science_hypothesis != marks_science_premise or marks_social_studies_hypothesis != marks_social_studies_premise or marks_english_hypothesis != marks_english_premise or marks_biology_hypothesis != marks_biology_premise:
    # check if the marks in any of the other subjects as per the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the marks as per the hypothesis do not contradict the premise, we infer neutral relation as the premise was an estimate for Math marks
    label = "neutral"

print(label)
