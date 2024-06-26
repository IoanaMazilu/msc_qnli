# Scores obtained by Nancy in different subjects according to the premise
marks_american_literature_premise = 66
marks_history_premise = 75
marks_home_economics_premise = 52
marks_physical_education_premise = 68
marks_art_premise = 89

# Scores obtained by Nancy in different subjects according to the hypothesis
marks_american_literature_hypothesis = 86
marks_history_hypothesis = 75
marks_home_economics_hypothesis = 52
marks_physical_education_hypothesis = 68
marks_art_hypothesis = 89

# Comparing the marks obtained by Nancy in different subjects according to the premise and the hypothesis
if marks_american_literature_premise!= marks_american_literature_hypothesis:
    # Checking if the marks obtained by Nancy in American Literature contradicts the premise
    label = "contradiction"
elif marks_history_premise!= marks_history_hypothesis or marks_home_economics_premise!= marks_home_economics_hypothesis or marks_physical_education_premise!= marks_physical_education_hypothesis or marks_art_premise!= marks_art_hypothesis:
    # Checking if the marks obtained by Nancy in other subjects contradicts the premise
    label = "contradiction"
else:
    # If the marks obtained by Nancy in different subjects according to the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
