literature_premise = 66
literature_hypothesis = 86
history_premise = 75
history_hypothesis = 75
home_economics_premise = 52
home_economics_hypothesis = 52
physical_education_premise = 68
physical_education_hypothesis = 68
art_premise = 89
art_hypothesis = 89

# the hypothesis refers to the marks obtained by Nancy in different subjects mentioned in the premise
if literature_hypothesis!= literature_premise:
    # check if the mark in Literature in the hypothesis contradicts the mark in Literature in the premise
    label = "contradiction"
elif history_hypothesis!= history_premise:
    # check if the mark in History in the hypothesis contradicts the mark in History in the premise
    label = "contradiction"
elif home_economics_hypothesis!= home_economics_premise:
    # check if the mark in Home Economics in the hypothesis contradicts the mark in Home Economics in the premise
    label = "contradiction"
elif physical_education_hypothesis!= physical_education_premise:
    # check if the mark in Physical Education in the hypothesis contradicts the mark in Physical Education in the premise
    label = "contradiction"
elif art_hypothesis!= art_premise:
    # check if the mark in Art in the hypothesis contradicts the mark in Art in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
