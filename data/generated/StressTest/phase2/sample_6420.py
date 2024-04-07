# Premise: Arun obtained 76, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Chemistry, Biology and Physics.
# Hypothesis: Arun obtained more than 66, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Chemistry, Biology and Physics.
# Golden Label: entailment

english_mark_premise = 76
math_mark_premise = 65
chemistry_mark_premise = 82
biology_mark_premise = 67
physics_mark_premise = 85

english_mark_hypothesis = 66
math_mark_hypothesis = 65
chemistry_mark_hypothesis = 82
biology_mark_hypothesis = 67
physics_mark_hypothesis = 85

# the hypothesis refers to Arun's marks in each subject mentioned in the premise
if english_mark_premise <= english_mark_hypothesis or math_mark_premise <= math_mark_hypothesis or chemistry_mark_premise <= chemistry_mark_hypothesis or biology_mark_premise <= biology_mark_hypothesis or physics_mark_premise <= physics_mark_hypothesis:
    # check if the hypothesis values contradict the marks in the premise
    label = "contradiction"
elif english_mark_premise > english_mark_hypothesis and math_mark_premise > math_mark_hypothesis and chemistry_mark_premise > chemistry_mark_hypothesis and biology_mark_premise > biology_mark_hypothesis and physics_mark_premise > physics_mark_hypothesis:
    # check if the hypothesis values are entailed by the premise marks
    label = "entailment"
else:
    # if the hypothesis values do not contradict or are not fully entailed by the premise ones, we infer neutrality
    label = "neutral"

print(label)

