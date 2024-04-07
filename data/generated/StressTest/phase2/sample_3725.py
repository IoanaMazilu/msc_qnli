# Premise: Dacid obtained 96, 98, 99, 100 and 98 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 16, 98, 99, 100 and 98 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

# Scores obtained by Dacid in different subjects as per premise
english_score_premise = 96
mathematics_score_premise = 98
physics_score_premise = 99
chemistry_score_premise = 100
biology_score_premise = 98

# Scores obtained by Dacid in different subjects as per hypothesis
english_score_hypothesis = 16
mathematics_score_hypothesis = 98
physics_score_hypothesis = 99
chemistry_score_hypothesis = 100
biology_score_hypothesis = 98

# Comparing the scores in the different subjects as per the premise and hypothesis
if (english_score_premise != english_score_hypothesis or 
    mathematics_score_premise != mathematics_score_hypothesis or 
    physics_score_premise != physics_score_hypothesis or 
    chemistry_score_premise != chemistry_score_hypothesis or 
    biology_score_premise != biology_score_hypothesis):
    # If any of the scores in any subject are different in the premise and hypothesis, it's a contradiction
    label = "contradiction"
else:
    # If all the scores in all subjects are the same in the premise and hypothesis, it's an entailment
    label = "entailment"

print(label)

