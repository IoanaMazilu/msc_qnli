# Scores obtained by Nancy in different subjects as per premise and hypothesis
literature_premise = 66
history_premise = 75
home_economics_premise = 52
physical_education_premise = 68
art_premise = 89

literature_hypothesis = 86
history_hypothesis = 75
home_economics_hypothesis = 52
physical_education_hypothesis = 68
art_hypothesis = 89

# Check if the scores obtained by Nancy in different subjects as per premise and hypothesis contradict each other
if literature_premise >= literature_hypothesis or history_premise > history_hypothesis or home_economics_premise > home_economics_hypothesis or physical_education_premise > physical_education_hypothesis or art_premise > art_hypothesis:
    label = "contradiction"
elif literature_premise < literature_hypothesis and history_premise == history_hypothesis and home_economics_premise == home_economics_hypothesis and physical_education_premise == physical_education_hypothesis and art_premise == art_hypothesis:
    label = "entailment"
else:
    label = "neutral"

print(label)
