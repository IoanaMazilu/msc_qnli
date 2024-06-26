student_ranking_premise = 15
student_ranking_hypothesis = 75

if student_ranking_hypothesis >= student_ranking_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
