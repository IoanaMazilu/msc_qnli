requirement_premise = 1/4
requirement_hypothesis = 3/4
members = 770

# the hypothesis talks about the requirement for a film to be considered for "movie of the year", same as the premise
if requirement_hypothesis < requirement_premise:
    # check if the requirement in the hypothesis contradicts the requirement in the premise
    label = "contradiction"
elif requirement_hypothesis == requirement_premise:
    # check if the requirement in the hypothesis matches exactly with the requirement in the premise
    label = "entailment"
else:
    # the premise gives a minimum requirement for the movie to be considered
    # while the requirement in the hypothesis is stricter, it does not contradict the premise
    label = "neutral"

print(label)
