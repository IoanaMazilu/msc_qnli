# Premise: Nancy obtained 66, 75, 52, 68 and 89 marks (out of 100) in American Literature, History, Home Economics, Physical Education and Art.
# Hypothesis: Nancy obtained 86, 75, 52, 68 and 89 marks (out of 100) in American Literature, History, Home Economics, Physical Education and Art.
# Golden Label: contradiction

# Defining marks in each subject for premise and hypothesis
american_literature_premise = 66
history_premise = 75
home_economics_premise = 52
physical_education_premise = 68
art_premise = 89

american_literature_hypothesis = 86
history_hypothesis = 75
home_economics_hypothesis = 52
physical_education_hypothesis = 68
art_hypothesis = 89

# Checking if marks obtained in each subject in hypothesis contradict those in the premise
if american_literature_hypothesis != american_literature_premise:
    label = "contradiction"
elif history_hypothesis != history_premise:
    label = "contradiction"
elif home_economics_hypothesis != home_economics_premise:
    label = "contradiction"
elif physical_education_hypothesis != physical_education_premise:
    label = "contradiction"
elif art_hypothesis != art_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)

