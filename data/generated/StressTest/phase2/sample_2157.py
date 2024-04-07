# Premise: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 775 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least less than 4/4 of the top-10-movies lists submitted by the Cinematic Academy’s 775 members.
# Golden Label: entailment

premise_ratio = 1/4
hypothesis_ratio = 4/4
members_premise = 775
members_hypothesis = 775

# the hypothesis refers to the ratio of lists in which a movie must appear to be considered for "movie of the year"
if premise_ratio != hypothesis_ratio or members_premise != members_hypothesis:
    # check if the ratio or the number of members in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the ratio and number of members from the hypothesis do not contradict those from the premise
    # we can infer entailment
    label = "entailment"

print(label)

