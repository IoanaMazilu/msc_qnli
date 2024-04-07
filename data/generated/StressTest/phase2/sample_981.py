# Premise: Dacid obtained 72, 45, 72, 77 and 75 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 42, 45, 72, 77 and 75 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

# Define variables for each subject score in premise and hypothesis
english_score_premise = 72
math_score_premise = 45
physics_score_premise = 72
chemistry_score_premise = 77
biology_score_premise = 75

english_score_hypothesis = 42
math_score_hypothesis = 45
physics_score_hypothesis = 72
chemistry_score_hypothesis = 77
biology_score_hypothesis = 75

# Compare each subject score in premise and hypothesis
if english_score_premise <= english_score_hypothesis:
    # check if the english score in the hypothesis contradicts the english score in the premise
    label = "contradiction"
elif math_score_premise != math_score_hypothesis:
    # check if the math score in the hypothesis contradicts the math score in the premise
    label = "contradiction"
elif physics_score_premise != physics_score_hypothesis:
    # check if the physics score in the hypothesis contradicts the physics score in the premise
    label = "contradiction"
elif chemistry_score_premise != chemistry_score_hypothesis:
    # check if the chemistry score in the hypothesis contradicts the chemistry score in the premise
    label = "contradiction"
elif biology_score_premise != biology_score_hypothesis:
    # check if the biology score in the hypothesis contradicts the biology score in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

