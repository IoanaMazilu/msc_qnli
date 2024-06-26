student_ranking_premise = 24
student_ranking_hypothesis = 74

if student_ranking_hypothesis >= student_ranking_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
