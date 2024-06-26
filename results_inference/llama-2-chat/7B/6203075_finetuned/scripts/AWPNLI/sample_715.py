papers_per_cousin = 48.0
cousins_number = 6.0
papers_given_per_cousin = 289.0

# the hypothesis refers to the number of papers given to the cousins, which is also mentioned in the premise
# compute the total number of papers given in the premise
total_papers_given_premise = papers_per_cousin * cousins_number

if papers_given_per_cousin!= total_papers_given_premise:
    # check if the number of papers given in the hypothesis contradicts the number of papers given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
