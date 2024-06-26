relatives_visit_premise = 1
cousins_premise = 6
origami_papers_premise = 48.0
given_papers_premise = 289.0

# the hypothesis refers to the number of origami papers given away, which are also mentioned in the premise
# compute the total number of origami papers given away per cousin
total_papers_per_cousin_premise = given_papers_premise / cousins_premise
if total_papers_per_cousin_premise!= origami_papers_premise:
    # check if the number of origami papers given away per cousin in the hypothesis contradicts the number of origami papers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
