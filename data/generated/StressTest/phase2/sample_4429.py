# Premise: To be considered for “ movie of the year, ” a film must appear in at least less than 8/4 of the top-10-movies lists submitted by the Cinematic Academy’s 765 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 765 members.
# Golden Label: neutral

required_lists_premise = 8/4
required_lists_hypothesis = 1/4
members_premise = 765
members_hypothesis = 765

# the hypothesis refers to the same conditions for a film to be considered for "movie of the year"
if required_lists_hypothesis != required_lists_premise:
    # check if the fraction of required lists in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
elif members_hypothesis != members_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

