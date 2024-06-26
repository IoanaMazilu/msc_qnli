paper_length_premise = 56
paper_length_hypothesis = 66
due_days_premise = 6
due_days_hypothesis = 6

# the hypothesis refers to the length of a history paper and the due date, both mentioned in the premise
if paper_length_hypothesis <= paper_length_premise:
    # check if the length of the history paper in the hypothesis contradicts the estimate of more than 'paper_length_premise'
    label = "contradiction"
elif due_days_hypothesis!= due_days_premise:
    # check if the due date in the hypothesis contradicts the due date reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the history paper
    # any length greater than 'paper_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
