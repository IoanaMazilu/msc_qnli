marks_english_premise = 16
marks_english_hypothesis = 86

marks_math_premise = 89
marks_math_hypothesis = 89

marks_physics_premise = 82
marks_physics_hypothesis = 82

marks_chemistry_premise = 87
marks_chemistry_hypothesis = 87

marks_biology_premise = 81
marks_biology_hypothesis = 81

# the hypothesis talks about the marks obtained by Dacid in various subjects, referenced also in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the hypothesis value contradicts the estimate of more than 'marks_english_premise' in English
    label = "contradiction"
elif marks_math_hypothesis != marks_math_premise or marks_physics_hypothesis != marks_physics_premise or marks_chemistry_hypothesis != marks_chemistry_premise or marks_biology_hypothesis != marks_biology_premise:
    # check if the hypothesis values contradict the exact marks reported in the premise for the other subjects
    label = "contradiction"
else:
    # the premise gives only an estimate for the English marks
    # any number of marks greater than 'marks_english_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
