# Premise: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 795 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least less than 2/4 of the top-10-movies lists submitted by the Cinematic Academy’s 795 members.
# Golden Label: entailment

lists_premise = 1/4
lists_hypothesis = 2/4

# the hypothesis refers to the number of top-10-movies lists needed for a film to be considered for the "movie of the year"
if lists_hypothesis >= lists_premise:
    # check if the hypothesis value contradicts the estimate of at least 'lists_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

