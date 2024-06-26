premise_lists = 1/4
hypothesis_lists = 4/4

# hypothesis refers to the fraction of top-10-movies lists that a movie must appear in to be considered for 'movie of the year'
# this is in direct comparison with the premise
if premise_lists > hypothesis_lists:
    # check if the fraction from the hypothesis contradicts the one from the premise
    label = "contradiction"
elif premise_lists < hypothesis_lists:
    # check if the fraction from the hypothesis can be fully and explicitly entailed from the one in the premise
    label = "entailment"
else:
    # if the fractions are equal, then there is no contradiction or entailment
    label = "neutral"

print(label)
