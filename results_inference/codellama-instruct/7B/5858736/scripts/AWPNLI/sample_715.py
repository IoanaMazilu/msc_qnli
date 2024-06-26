premise_cousins = 6.0
premise_given_papers = 48.0
premise_origami_papers = premise_given_papers / premise_cousins

hypothesis_given_papers = 289.0

# the hypothesis refers to the number of papers given away, which is also mentioned in the premise
# compute the total number of origami papers in the premise
total_origami_papers_premise = premise_given_papers / premise_cousins

if hypothesis_given_papers!= total_origami_papers_premise:
    # check if the number of papers given away in the hypothesis contradicts the number of origami papers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
