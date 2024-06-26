# Scores obtained by Nancy in different subjects according to the premise
american_literature_premise = 66
history_premise = 75
home_economics_premise = 52
physical_education_premise = 68
art_premise = 89

# Scores obtained by Nancy in different subjects according to the hypothesis
american_literature_hypothesis = 86
history_hypothesis = 75
home_economics_hypothesis = 52
physical_education_hypothesis = 68
art_hypothesis = 89

# Comparison between the scores obtained by Nancy according to the premise and the hypothesis
if american_literature_premise >= american_literature_hypothesis:
    # Check if the score obtained by Nancy in American Literature according to the hypothesis contradicts the score obtained according to the premise
    label = "contradiction"
elif history_premise!= history_hypothesis or home_economics_premise!= home_economics_hypothesis or physical_education_premise!= physical_education_hypothesis or art_premise!= art_hypothesis:
    # Check if the scores obtained by Nancy in other subjects according to the hypothesis contradict the scores obtained according to the premise
    label = "contradiction"
else:
    # If the scores obtained by Nancy according to the hypothesis do not contradict the scores obtained according to the premise, we can infer entailment
    label = "entailment"

print(label)
