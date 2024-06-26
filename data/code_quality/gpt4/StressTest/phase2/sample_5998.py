list_presence_premise = 4/4
list_presence_hypothesis = 1/4
members_premise = 760
members_hypothesis = 760

# the hypothesis refers to the condition for a movie to be considered for the movie of the year, mentioned in the premise
if members_premise != members_hypothesis:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
elif list_presence_hypothesis > list_presence_premise:
    # check if the condition in the hypothesis contradicts the condition (less than 4/4) in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the list presence
    # any list presence less than 4/4 is consistent with the premise, so we can infer entailment
    label = "entailment"

print(label)
