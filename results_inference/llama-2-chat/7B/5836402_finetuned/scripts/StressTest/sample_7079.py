paper_pages_premise = 66
paper_pages_hypothesis = 66
days_premise = 6
days_hypothesis = 6

# the hypothesis refers to the number of pages of the history paper and the number of days left for the submission
if paper_pages_hypothesis <= paper_pages_premise:
    # check if the hypothesis value contradicts the number of pages in the premise
    label = "contradiction"
elif days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
