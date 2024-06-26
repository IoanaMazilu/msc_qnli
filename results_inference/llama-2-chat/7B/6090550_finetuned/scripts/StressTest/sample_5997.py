# The premise and hypothesis are talking about the same topic

# The hypothesis refers to the percentage of top-10 movies lists that a film must appear in
# to be considered for movie of the year

percentage_hypothesis = 4/4

# The premise specifies the percentage of top-10 movies lists that a film must appear in
# to be considered for movie of the year
percentage_premise = 1/4

if percentage_hypothesis!= percentage_premise:
    # Check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # If the percentages are the same, we can infer entailment
    label = "entailment"

print(label)
