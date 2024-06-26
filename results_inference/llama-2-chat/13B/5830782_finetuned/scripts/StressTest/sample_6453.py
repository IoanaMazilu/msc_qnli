# Scores from the premise
english_premise = 66
math_premise = 60
chemistry_premise = 72
biology_premise = 77
french_premise = 55
physics_premise = 85

# Scores from the hypothesis
english_hypothesis = 76
math_hypothesis = 60
chemistry_hypothesis = 72
biology_hypothesis = 77
french_hypothesis = 55
physics_hypothesis = 85

# The hypothesis refers to the scores from the premise
if english_hypothesis <= english_premise:
    # Check if the English score in the hypothesis contradicts the English score in the premise
    label = "contradiction"
elif math_hypothesis!= math_premise or chemistry_hypothesis!= chemistry_premise or biology_hypothesis!= biology_premise or french_hypothesis!= french_premise or physics_hypothesis!= physics_premise:
    # Check if the other scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
else:
    # If all the scores in the hypothesis are less than the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
