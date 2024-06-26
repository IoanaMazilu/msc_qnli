# defining the marks obtained by Nancy in each subject according to the premise
american_literature_premise = 66
history_premise = 75
home_economics_premise = 52
physical_education_premise = 68
art_premise = 89

# defining the marks obtained by Nancy in each subject according to the hypothesis
american_literature_hypothesis = 86
history_hypothesis = 75
home_economics_hypothesis = 52
physical_education_hypothesis = 68
art_hypothesis = 89

# the hypothesis refers to the marks obtained by Nancy in each subject mentioned in the premise
if american_literature_hypothesis!= american_literature_premise:
    # check if the marks obtained in American Literature according to the hypothesis contradicts the marks obtained according to the premise
    label = "contradiction"
elif history_hypothesis!= history_premise or home_economics_hypothesis!= home_economics_premise or physical_education_hypothesis!= physical_education_premise or art_hypothesis!= art_premise:
    # check if the marks obtained in any other subject according to the hypothesis contradicts the marks obtained according to the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
