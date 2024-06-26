paper_pages_premise = 63
paper_pages_hypothesis = 33
due_days_premise = 3
due_days_hypothesis = 3

# the hypothesis refers to the length of Stacy's history paper and when it's due, both mentioned in the premise
if paper_pages_hypothesis >= paper_pages_premise:
    # check if the length of the paper in the hypothesis contradicts the estimate of less than 'paper_pages_premise'
    label = "contradiction"
elif due_days_hypothesis != due_days_premise:
    # check if the due date in the hypothesis contradicts the due date in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the paper
    # any length less than 'paper_pages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
