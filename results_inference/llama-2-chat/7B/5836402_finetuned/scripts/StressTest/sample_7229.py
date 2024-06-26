# Define variables for each subject and their corresponding marks in the premise
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

# The hypothesis refers to the same subjects and marks as the premise
if american_literature_hypothesis!= american_literature_premise:
    # Check if the American Literature mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif history_hypothesis!= history_premise:
    # Check if the History mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif home_economics_hypothesis!= home_economics_premise:
    # Check if the Home Economics mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif physical_education_hypothesis!= physical_education_premise:
    # Check if the Physical Education mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
elif art_hypothesis!= art_premise:
    # Check if the Art mark in the hypothesis contradicts the mark in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
