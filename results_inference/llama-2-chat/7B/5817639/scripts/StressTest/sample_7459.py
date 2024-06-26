top_movies_premise = 2/4
top_movies_hypothesis = 1/4

# the hypothesis refers to the fraction of top-10 movies lists that a film must appear in to be considered for movie of the year
if top_movies_premise <= top_movies_hypothesis:
    # check if the estimate of 'top_movies_hypothesis' contradicts the fraction of top-10 movies lists in the premise
    label = "contradiction"
elif top_movies_hypothesis!= top_movies_premise:
    # check if the hypothesis value contradicts the estimate of the fraction of top-10 movies lists in the premise
    label = "contradiction"
else:
    # if the hypothesis value is consistent with the premise value, we can infer entailment
    label = "entailment"

print(label)
