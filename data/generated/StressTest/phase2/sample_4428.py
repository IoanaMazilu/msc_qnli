# Premise: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 765 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least less than 8/4 of the top-10-movies lists submitted by the Cinematic Academy’s 765 members.
# Golden Label: entailment

min_appearances_premise = 1/4
min_appearances_hypothesis = 8/4
members_premise = 765
members_hypothesis = 765

# the hypothesis talks about the minimum appearances in the top-10-movies lists and the number of members of the Cinematic Academy, both referenced in the premise
if min_appearances_hypothesis > min_appearances_premise:
    # check if the minimum appearances ratio in the hypothesis contradicts the same ratio in the premise
    label = "contradiction"
elif members_hypothesis != members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

