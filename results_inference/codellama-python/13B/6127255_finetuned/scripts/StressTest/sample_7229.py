literature_mark_premise = 66
history_mark_premise = 75
home_economics_mark_premise = 52
physical_education_mark_premise = 68
art_mark_premise = 89

literature_mark_hypothesis = 86
history_mark_hypothesis = 75
home_economics_mark_hypothesis = 52
physical_education_mark_hypothesis = 68
art_mark_hypothesis = 89

# the hypothesis refers to the marks obtained by Nancy in different subjects mentioned in the premise
if literature_mark_hypothesis!= literature_mark_premise:
    # check if the mark in literature in the hypothesis contradicts the mark in literature in the premise
    label = "contradiction"
elif history_mark_hypothesis!= history_mark_premise or home_economics_mark_hypothesis!= home_economics_mark_premise or physical_education_mark_hypothesis!= physical_education_mark_premise or art_mark_hypothesis!= art_mark_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks in the same subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
