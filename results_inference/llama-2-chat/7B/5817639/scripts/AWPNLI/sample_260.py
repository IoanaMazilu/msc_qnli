pieces_of_paper_premise = float(900.0)
pieces_of_paper_hypothesis = float(744.0)

# compare the number of pieces of paper left according to the hypothesis and the premise
if pieces_of_paper_hypothesis >= pieces_of_paper_premise:
    # check if the number of pieces of paper left according to the hypothesis contradicts the number of pieces of paper used in the premise
    label = "contradiction"
elif pieces_of_paper_hypothesis - pieces_of_paper_premise!= 0:
    # check if the number of pieces of paper left according to the hypothesis contradicts the number of pieces of paper used in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
