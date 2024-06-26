top_10_movies_lists_premise = 2/4
top_10_movies_lists_hypothesis = 1/4

# the hypothesis refers to the fraction of top-10-movies lists a film must appear in, mentioned in the premise
if top_10_movies_lists_hypothesis!= top_10_movies_lists_premise:
    # check if the fraction in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
