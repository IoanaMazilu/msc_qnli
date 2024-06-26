# Marks obtained by Nancy in the subjects as per the premise
lit_marks_premise = 66
history_marks_premise = 75
home_eco_marks_premise = 52
phy_edu_marks_premise = 68
art_marks_premise = 89

# Marks obtained by Nancy in the subjects as per the hypothesis
lit_marks_hypothesis = 86
history_marks_hypothesis = 75
home_eco_marks_hypothesis = 52
phy_edu_marks_hypothesis = 68
art_marks_hypothesis = 89

# Compare the marks obtained in each subject as per the premise and hypothesis
if lit_marks_premise >= lit_marks_hypothesis:
    # Check if the marks obtained in Literature as per the hypothesis contradicts the marks obtained as per the premise
    label = "contradiction"
elif history_marks_premise != history_marks_hypothesis or home_eco_marks_premise != home_eco_marks_hypothesis or phy_edu_marks_premise != phy_edu_marks_hypothesis or art_marks_premise != art_marks_hypothesis:
    # Check if the marks obtained in any other subject as per the hypothesis contradicts the marks obtained as per the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
