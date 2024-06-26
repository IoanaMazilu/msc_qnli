french_mark_premise = 86
french_mark_hypothesis = 86
geography_mark_premise = 75
geography_mark_hypothesis = 75
art_design_mark_premise = 72
art_design_mark_hypothesis = 72
history_mark_premise = 63
history_mark_hypothesis = 63
physical_education_mark_premise = 65
physical_education_mark_hypothesis = 65

# the hypothesis refers to the marks scored by Adam in various subjects mentioned in the premise
if french_mark_hypothesis <= french_mark_premise:
    # check if the hypothesis value contradicts the exact mark in French Language in the premise
    label = "contradiction"
elif geography_mark_hypothesis!= geography_mark_premise or art_design_mark_hypothesis!= art_design_mark_premise or history_mark_hypothesis!= history_mark_premise or physical_education_mark_hypothesis!= physical_education_mark_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
