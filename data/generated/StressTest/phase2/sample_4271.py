# Premise: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 785 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least less than 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 785 members.
# Golden Label: contradiction

list_percentage_premise = 0.25
list_percentage_hypothesis = 0.25
members_premise = 785
members_hypothesis = 785

# the hypothesis talks about the requirement of appearing in top-10-movies lists for a film to be considered for "movie of the year"
# this requirement is also mentioned in the premise
if list_percentage_hypothesis > list_percentage_premise or members_hypothesis != members_premise:
    # check if the requirement in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif list_percentage_hypothesis == list_percentage_premise and members_hypothesis == members_premise:
    # check if the requirement in the hypothesis is the same as the one in the premise
    label = "entailment"
else:
    # if the requirement in the hypothesis does not contradict the one in the premise, but is not the same either,
    # we can infer the relationship is neutral
    label = "neutral"

print(label)

