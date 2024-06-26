american_literature_premise = 86
american_literature_hypothesis = 66
history_premise = 75
history_hypothesis = 75
home_economics_premise = 52
home_economics_hypothesis = 52
physical_education_premise = 68
physical_education_hypothesis = 68
art_premise = 89
art_hypothesis = 89

# the hypothesis refers to the marks obtained by Nancy in various subjects mentioned in the premise
if american_literature_hypothesis >= american_literature_premise:
    # check if the mark obtained in American Literature in the hypothesis contradicts the premise
    label = "contradiction"
elif history_hypothesis!= history_premise or home_economics_hypothesis!= home_economics_premise or physical_education_hypothesis!= physical_education_premise or art_hypothesis!= art_premise:
    # check if the marks obtained in other subjects in the hypothesis contradict the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the mark in American Literature
    # any mark less than 'american_literature_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
