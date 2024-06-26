lists_premise = 1/4
lists_hypothesis = 1/4
total_members_premise = 775
total_members_hypothesis = 775

# the hypothesis refers to the same condition for considering a film for "movie of the year", mentioned in the premise
if lists_hypothesis >= lists_premise:
    # check if the 'lists_hypothesis' contradicts the condition in the premise
    label = "contradiction"
elif total_members_hypothesis != total_members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
