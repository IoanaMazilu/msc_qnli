english_marks_premise = 16
english_marks_hypothesis = 86

maths_marks_premise = 89
maths_marks_hypothesis = 89

physics_marks_premise = 82
physics_marks_hypothesis = 82

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 81
biology_marks_hypothesis = 81

# check if the hypothesis values contradict the premise values
if any([hypothesis_value < premise_value for hypothesis_value, premise_value in zip(
        (english_marks_hypothesis, maths_marks_hypothesis, physics_marks_hypothesis, chemistry_marks_hypothesis, biology_marks_hypothesis),
        (english_marks_premise, maths_marks_premise, physics_marks_premise, chemistry_marks_premise, biology_marks_premise))])):
    label = "contradiction"
elif any([premise_value!= hypothesis_value for hypothesis_value, premise_value in zip(
        (english_marks_hypothesis, maths_marks_hypothesis, physics_marks_hypothesis, chemistry_marks_hypothesis, biology_marks_hypothesis),
        (english_marks_premise, maths_marks_premise, physics_marks_premise, chemistry_marks_premise, biology_marks_premise))]).any():
    label = "neutral"
else:
    label = "entailment"

print(label)
