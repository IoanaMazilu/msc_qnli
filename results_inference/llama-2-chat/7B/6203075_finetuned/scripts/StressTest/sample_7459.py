percentage_of_lists_premise = 2/4
percentage_of_lists_hypothesis = 1/4

# the hypothesis refers to the percentage of top-10 movie lists a film must appear in to be considered for movie of the year
if percentage_of_lists_hypothesis!= percentage_of_lists_premise:
    # check if the percentage of lists in the hypothesis contradicts the percentage of lists in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
