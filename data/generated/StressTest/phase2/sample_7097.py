# Premise: Nitin ranks 15 th in a class of 47 students.
# Hypothesis: Nitin ranks 65 th in a class of 47 students.
# Golden Label: contradiction

nitin_rank_premise = 15
class_size_premise = 47
nitin_rank_hypothesis = 65
class_size_hypothesis = 47

# the hypothesis refers to Nitin's rank and the class size in the premise
if nitin_rank_hypothesis > class_size_hypothesis:
    # check if Nitin's rank in hypothesis contradicts the class size in the premise
    label = "contradiction"
elif nitin_rank_hypothesis != nitin_rank_premise:
    # check if Nitin's rank in the hypothesis contradicts his rank in the premise
    label = "contradiction"
else:
    label = "neutral"

print(label)

