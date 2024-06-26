marks_math_premise = 46
marks_math_hypothesis = 76
marks_science_premise = 65
marks_science_hypothesis = 65
marks_social_studies_premise = 82
marks_social_studies_hypothesis = 82
marks_english_premise = 67
marks_english_hypothesis = 67
marks_biology_premise = 75
marks_biology_hypothesis = 75

# the hypothesis refers to the exact scores in each subject, mentioned in the premise
if marks_math_hypothesis <= marks_math_premise:
    # check if the hypothesis value contradicts the estimate of more than'marks_math_premise'
    label = "contradiction"
elif marks_science_hypothesis!= marks_science_premise:
    # check if the hypothesis value contradicts the exact score in science mentioned in the premise
    label = "contradiction"
elif marks_social_studies_hypothesis!= marks_social_studies_premise:
    # check if the hypothesis value contradicts the exact score in social studies mentioned in the premise
    label = "contradiction"
elif marks_english_hypothesis!= marks_english_premise:
    # check if the hypothesis value contradicts the exact score in english mentioned in the premise
    label = "contradiction"
elif marks_biology_hypothesis!= marks_biology_premise:
    # check if the hypothesis value contradicts the exact score in biology mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
