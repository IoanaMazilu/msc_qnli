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
if literature_premise >= literature_hypothesis:
    # check if the estimate of 'literature_hypothesis' contradicts the mark obtained in Literature in the premise
    label = "contradiction"
elif history_premise!= history_hypothesis:
    # check if the mark obtained in History in the hypothesis contradicts the mark obtained in History reported in the premise
    label = "contradiction"
elif home_economics_premise!= home_economics_hypothesis:
    # check if the mark obtained in Home Economics in the hypothesis contradicts the mark obtained in Home Economics reported in the premise
    label = "contradiction"
elif physical_education_premise!= physical_education_hypothesis:
    # check if the mark obtained in Physical Education in the hypothesis contradicts the mark obtained in Physical Education reported in the premise
    label = "contradiction"
elif art_premise!= art_hypothesis:
    # check if the mark obtained in Art in the hypothesis contradicts the mark obtained in Art reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
