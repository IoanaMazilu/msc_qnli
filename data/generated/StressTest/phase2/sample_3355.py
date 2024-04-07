# Premise: To be considered for “ movie of the year, ” a film must appear in at least less than 2/4 of the top-10-movies lists submitted by the Cinematic Academy’s 795 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 795 members.
# Golden Label: neutral

top_list_premise = 2/4
top_list_hypothesis = 1/4
members_premise = 795
members_hypothesis = 795

# the hypothesis refers to the number of top list appearances and members, also mentioned in the premise
if top_list_hypothesis >= top_list_premise:
    # check if the number of top list appearances in the hypothesis contradicts the less than 'top_list_premise' in the premise
    label = "contradiction"
elif members_hypothesis != members_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

