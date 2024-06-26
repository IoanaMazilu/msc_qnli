# The hypothesis and premise are about the percentage of top-10 movies lists that a film must appear in to be considered for "movie of the year".
percentage_premise = 1/4
percentage_hypothesis = 3/4

# The hypothesis refers to a percentage that is greater than the premise
if percentage_hypothesis <= percentage_premise:
    # Check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # If the percentage in the hypothesis is greater than the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
