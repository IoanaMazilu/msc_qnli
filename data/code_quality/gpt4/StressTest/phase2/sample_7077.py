paper_length_premise = 66
paper_length_hypothesis = 56
due_days_premise = 6
due_days_hypothesis = 6

# the hypothesis refers to the length of the paper and the due date mentioned in the premise
if paper_length_premise <= paper_length_hypothesis:
    # check if the estimate of 'paper_length_hypothesis' contradicts the length of the paper in the premise
    label = "contradiction"
elif due_days_hypothesis != due_days_premise:
    # check if the due date in the hypothesis contradicts the due date reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
