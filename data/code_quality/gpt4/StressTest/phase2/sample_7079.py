paper_length_premise = 66
paper_length_hypothesis = 66
days_due_premise = 6
days_due_hypothesis = 6

# the hypothesis refers to the length and due date of Stacy's history paper mentioned in the premise
if paper_length_hypothesis <= paper_length_premise:
    # check if the estimate of 'paper_length_hypothesis' contradicts the length of the paper in the premise
    label = "contradiction"
elif days_due_hypothesis != days_due_premise:
    # check if the due date in the hypothesis contradicts the due date reported in the premise
    label = "contradiction"
else:
    # the premise provides exact values for the length and due date of the paper
    # a length greater than 'paper_length_premise' is inconsistent with the premise
    label = "contradiction"

print(label)
