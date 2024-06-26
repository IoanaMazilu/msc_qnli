english_marks_premise = 86
english_marks_hypothesis = 56
mathematics_marks_premise = 89
mathematics_marks_hypothesis = 89
physics_marks_premise = 82
physics_marks_hypothesis = 82
chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87
biology_marks_premise = 81
biology_marks_hypothesis = 81

# check if the hypothesis values contradict the premise values
if any([h < p for h, p in zip(english_marks_hypothesis, english_marks_premise),
       h < p for h, p in zip(mathematics_marks_hypothesis, mathematics_marks_premise),
       h < p for h, p in zip(physics_marks_hypothesis, physics_marks_premise),
       h < p for h, p in zip(chemistry_marks_hypothesis, chemistry_marks_premise),
       h < p for h, p in zip(biology_marks_hypothesis, biology_marks_premise)]):
    label = "contradiction"
elif any([h > p for h, p in zip(english_marks_hypothesis, english_marks_premise),
           h > p for h, p in zip(mathematics_marks_hypothesis, mathematics_marks_premise),
           h > p for h, p in zip(physics_marks_hypothesis, physics_marks_premise),
           h > p for h, p in zip(chemistry_marks_hypothesis, chemistry_marks_premise),
           h > p for h, p in zip(biology_marks_hypothesis, biology_marks_premise)]):
    label = "entailment"
else:
    label = "neutral"

print(label)
