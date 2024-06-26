papers_premise = 48.0 / 1.0
papers_hypothesis = 289.0

# the hypothesis refers to the number of papers given away, which is also mentioned in the premise
# compute the number of papers given away in the premise
papers_premise_given = papers_premise * 6.0
if papers_hypothesis!= papers_premise_given:
    # check if the number of papers given away in the hypothesis contradicts the number of papers given away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
