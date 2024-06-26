relative_visits_premise = 1.0
cousins_premise = 6.0
origami_papers_premise = 48.0
given_papers_hypothesis = 289.0

# compute the total number of origami papers given by the premise
total_papers_premise = relative_visits_premise * cousins_premise * origami_papers_premise

if given_papers_hypothesis > total_papers_premise:
    # check if the number of given papers in the hypothesis contradicts the estimate of more than 'total_papers_premise'
    label = "contradiction"
elif given_papers_hypothesis < total_papers_premise:
    # check if the number of given papers in the hypothesis does not contradict the estimate of less than 'total_papers_premise'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
