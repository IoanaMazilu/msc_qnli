# Premise: Nitin ranks 23 th in a class of 60 students.
# Hypothesis: Nitin ranks less than 33 th in a class of 60 students.
# Golden Label: entailment

nitin_rank_premise = 23
class_size_premise = 60
nitin_rank_hypothesis = 33
class_size_hypothesis = 60

# The hypothesis refers to Nitin's rank and the class size mentioned in the premise
if class_size_hypothesis != class_size_premise:
    # check if the size of the class in the hypothesis contradicts the size of the class in the premise
    label = "contradiction"
elif nitin_rank_hypothesis <= nitin_rank_premise:
    # check if Nitin's estimated rank in the hypothesis contradicts his rank in the premise
    label = "contradiction"
else:
    # the premise gives an exact rank for Nitin
    # any rank less than 'nitin_rank_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

