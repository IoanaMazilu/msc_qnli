papers_per_cousin_premise = 48.0
cousins_premise = 6.0
total_papers_given_hypothesis = 289.0

# the hypothesis refers to the total number of papers given away, which is also mentioned in the premise
# compute the total number of papers given away in the premise
total_papers_given_premise = papers_per_cousin_premise * cousins_premise
if total_papers_given_hypothesis!= total_papers_given_premise:
    # check if the total number of papers given away in the hypothesis contradicts the total number of papers given away from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
