papers_given_premise = 48.0 * 6.0
papers_given_hypothesis = 289.0

# the hypothesis refers to the number of papers given by Haley, which is also mentioned in the premise
if papers_given_hypothesis!= papers_given_premise:
    # check if the number of papers given in the hypothesis contradicts the number of papers given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
