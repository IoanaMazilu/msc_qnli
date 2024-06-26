given_papers_per_cousin_premise = 48.0
cousins_premise = 6.0
total_given_papers_hypothesis = 289.0

# the hypothesis refers to the total number of given papers, which can be computed from the premise
# compute the total number of given papers in the premise
total_given_papers_premise = given_papers_per_cousin_premise * cousins_premise
if total_given_papers_hypothesis != total_given_papers_premise:
    # check if the total number of given papers in the hypothesis contradicts the total number of given papers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
