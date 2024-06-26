# the hypothesis refers to the number of origami papers given away, which is also mentioned in the premise
papers_given_premise = 48
papers_given_hypothesis = 289

# compute the total number of papers given away in the premise
total_papers_given_premise = papers_given_premise * 6.0 / 1.0
if papers_given_hypothesis!= total_papers_given_premise:
    # check if the number of papers given away in the hypothesis contradicts the number of papers given away from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
