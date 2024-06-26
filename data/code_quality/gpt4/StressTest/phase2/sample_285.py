# marks obtained by David in different subjects according to the premise
marks_english_premise = 76
marks_mathematics_premise = 65
marks_physics_premise = 82
marks_chemistry_premise = 67
marks_biology_premise = 85

# marks obtained by David in different subjects according to the hypothesis
marks_english_hypothesis = 56
marks_mathematics_hypothesis = 65
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 67
marks_biology_hypothesis = 85

# compare the marks obtained by David in different subjects according to the premise and hypothesis
if marks_english_premise <= marks_english_hypothesis or marks_mathematics_premise != marks_mathematics_hypothesis or marks_physics_premise != marks_physics_hypothesis or marks_chemistry_premise != marks_chemistry_hypothesis or marks_biology_premise != marks_biology_hypothesis:
    # if the marks obtained by David in any subject according to the hypothesis contradicts the marks obtained according to the premise
    label = "contradiction"
elif marks_english_premise > marks_english_hypothesis:
    # if the marks obtained by David in English according to the premise is more than the marks obtained according to the hypothesis
    label = "entailment"
else:
    # if the marks obtained by David in all subjects according to the premise and hypothesis are same, we can infer entailment
    label = "entailment"

print(label)
