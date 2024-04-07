# Premise: Stacy has a more than 31 page history paper due in 3 days.
# Hypothesis: Stacy has a 81 page history paper due in 3 days.
# Golden Label: neutral

paper_length_premise = 31
paper_length_hypothesis = 81
due_days_premise = 3
due_days_hypothesis = 3

# the hypothesis refers to the length of the paper and the due date mentioned in the premise
if paper_length_hypothesis <= paper_length_premise:
    # check if the length of the paper in the hypothesis contradicts the minimum length of the paper in the premise
    label = "contradiction"
elif due_days_hypothesis != due_days_premise:
    # check if the due date in the hypothesis contradicts the due date in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the paper
    # any length greater than 'paper_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

