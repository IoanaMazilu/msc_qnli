# Premise: Nitin ranks 24 th in a class of 58 students.
# Hypothesis: Nitin ranks more than 24 th in a class of 58 students.
# Golden Label: contradiction

rank_premise = 24
rank_hypothesis = 24
students_premise = 58
students_hypothesis = 58

# the hypothesis refers to the rank and class size mentioned in the premise
if rank_hypothesis < rank_premise:
    # check if the rank in the hypothesis contradicts Nitin's rank in the premise
    label = "contradiction"
elif students_hypothesis != students_premise:
    # check if the class size in the hypothesis contradicts the class size mentioned in the premise
    label = "contradiction"
else:
    # the statement "Nitin ranks more than 24th" is ambiguous and can be interpreted as Nitin ranks worse than 24th
    # so, the hypothesis does not contradict the premise, but cannot be explicitly inferred from the premise
    label = "neutral"

print(label)

