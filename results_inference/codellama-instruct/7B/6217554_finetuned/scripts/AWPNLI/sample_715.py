# the hypothesis refers to the number of papers given away, which is also mentioned in the premise
# compute the total number of papers given away in the premise
total_papers_premise = 289.0

# compute the number of papers given away per cousin in the premise
papers_per_cousin_premise = 48.0
# compute the number of cousins in the premise
cousins_premise = 6.0
# compute the total number of cousins in the premise
total_cousins_premise = 1.0 * cousins_premise
# compute the total number of papers given away per cousin in the premise
total_papers_per_cousin_premise = papers_per_cousin_premise * total_cousins_premise
# compute the total number of papers given away in the premise
total_papers_premise = total_papers_per_cousin_premise * cousins_premise

if total_papers_hypothesis!= total_papers_premise:
    # check if the number of papers given away in the hypothesis contradicts the number of papers given away from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
