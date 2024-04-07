# Premise: Nitin ranks less than 77 th in a class of 89 students.
# Hypothesis: Nitin ranks 27 th in a class of 89 students.
# Golden Label: neutral

rank_premise = 77
rank_hypothesis = 27
class_size = 89

# the hypothesis refers to the rank of Nitin from the premise
if rank_hypothesis >= rank_premise:
    # check if the rank in the hypothesis contradicts the premise's statement of Nitin ranking less than 77
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank less than 77 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

