marks_english_premise = 76
marks_mathematics_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85
marks_total_premise = 46 + 65 + 82 + 67 + 85

marks_english_hypothesis = 46
marks_mathematics_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85
marks_total_hypothesis = 46 + 65 + 82 + 67 + 85

# the hypothesis talks about the marks obtained by Arun in each subject, referenced also in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_english_premise'
    label = "contradiction"
elif marks_mathematics_hypothesis <= marks_mathematics_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_mathematics_premise'
    label = "contradiction"
elif marks_chemistry_hypothesis <= marks_chemistry_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_chemistry_premise'
    label = "contradiction"
elif marks_biology_hypothesis <= marks_biology_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_biology_premise'
    label = "contradiction"
elif marks_physics_hypothesis <= marks_physics_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_physics_premise'
    label = "contradiction"
elif marks_total_hypothesis <= marks_total_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained by Arun in each subject
    # any number of marks greater than'marks_total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
