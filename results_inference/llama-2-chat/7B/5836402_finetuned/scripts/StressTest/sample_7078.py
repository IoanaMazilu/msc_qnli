paper_pages_premise = 56
paper_pages_hypothesis = 66
days_premise = 6
days_hypothesis = 6

# the hypothesis refers to the number of pages of the paper and the due date, both mentioned in the premise
if paper_pages_hypothesis <= paper_pages_premise:
    # check if the hypothesis value contradicts the estimate of more than 'paper_pages_premise'
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the due date in the hypothesis contradicts the due date in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
