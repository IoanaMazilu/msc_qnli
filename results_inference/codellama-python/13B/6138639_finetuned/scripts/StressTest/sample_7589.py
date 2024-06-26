french_language_premise = 86
french_language_hypothesis = 86
geography_premise = 75
geography_hypothesis = 75
art_design_premise = 72
art_design_hypothesis = 72
history_premise = 63
history_hypothesis = 63
physical_education_premise = 65
physical_education_hypothesis = 65

# the hypothesis refers to the marks of Adam in the subjects mentioned in the premise
if french_language_hypothesis <= french_language_premise:
    # check if the estimate of 'french_language_hypothesis' contradicts the mark in the premise
    label = "contradiction"
elif geography_hypothesis!= geography_premise:
    # check if the mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif art_design_hypothesis!= art_design_premise:
    # check if the mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif history_hypothesis!= history_premise:
    # check if the mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif physical_education_hypothesis!= physical_education_premise:
    # check if the mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
