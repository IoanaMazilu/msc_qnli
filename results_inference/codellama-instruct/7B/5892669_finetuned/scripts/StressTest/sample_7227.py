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
if american_literature_premise >= american_literature_hypothesis:
    # check if the estimate of 'american_literature_hypothesis' contradicts the mark obtained in American Literature in the premise
    label = "contradiction"
elif history_premise!= history_hypothesis or home_economics_premise!= home_economics_hypothesis or physical_education_premise!= physical_education_hypothesis or art_premise!= art_hypothesis:
    # check if the marks obtained in other subjects in the hypothesis contradict the marks obtained in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
