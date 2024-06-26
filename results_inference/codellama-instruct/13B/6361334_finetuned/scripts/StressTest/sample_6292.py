marks_english_premise = 46
marks_maths_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85

marks_english_hypothesis = 76
marks_maths_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in the mentioned subjects
if marks_english_hypothesis <= marks_english_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_english_premise'
    label = "contradiction"
elif marks_maths_hypothesis!= marks_maths_premise:
    # check if the hypothesis value contradicts the value of marks in mathematics reported in the premise
    label = "contradiction"
elif marks_chemistry_hypothesis!= marks_chemistry_premise:
    # check if the hypothesis value contradicts the value of marks in chemistry reported in the premise
    label = "contradiction"
elif marks_biology_hypothesis!= marks_biology_premise:
    # check if the hypothesis value contradicts the value of marks in biology reported in the premise
    label = "contradiction"
elif marks_physics_hypothesis!= marks_physics_premise:
    # check if the hypothesis value contradicts the value of marks in physics reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)