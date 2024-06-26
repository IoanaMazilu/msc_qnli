nancy_american_literature_premise = 86
nancy_american_literature_hypothesis = 66
nancy_history_premise = 75
nancy_history_hypothesis = 75
nancy_home_economics_premise = 52
nancy_home_economics_hypothesis = 52
nancy_physical_education_premise = 68
nancy_physical_education_hypothesis = 68
nancy_art_premise = 89
nancy_art_hypothesis = 89

# the hypothesis refers to the exact marks obtained by Nancy in each subject
if nancy_american_literature_hypothesis!= nancy_american_literature_premise:
    # check if the hypothesis value contradicts the premise value for American Literature
    label = "contradiction"
elif nancy_history_hypothesis!= nancy_history_premise:
    # check if the hypothesis value contradicts the premise value for History
    label = "contradiction"
elif nancy_home_economics_hypothesis!= nancy_home_economics_premise:
    # check if the hypothesis value contradicts the premise value for Home Economics
    label = "contradiction"
elif nancy_physical_education_hypothesis!= nancy_physical_education_premise:
    # check if the hypothesis value contradicts the premise value for Physical Education
    label = "contradiction"
elif nancy_art_hypothesis!= nancy_art_premise:
    # check if the hypothesis value contradicts the premise value for Art
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
