relatives_visit_premise = 1
cousins_premise = 6
origami_papers_premise = 48
given_papers_premise = 289

# the hypothesis refers to the number of origami papers given away, which are also mentioned in the premise
# compute the total number of origami papers given away by Haley and her cousins
total_given_papers = given_papers_premise / cousins_premise
if total_given_papers!= origami_papers_premise:
    # check if the number of origami papers given away in the hypothesis contradicts the number of origami papers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
