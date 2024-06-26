visited_cousins_premise = 6.0
origami_papers_premise = 48.0
total_origami_papers_hypothesis = 289.0

# the hypothesis talks about the number of origami papers given away, which is also referenced in the premise
# compute the total number of origami papers given away in the premise
total_origami_papers_premise = visited_cousins_premise * origami_papers_premise
if total_origami_papers_hypothesis!= total_origami_papers_premise:
    # check if the number of origami papers given away in the hypothesis contradicts the number of papers given away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
