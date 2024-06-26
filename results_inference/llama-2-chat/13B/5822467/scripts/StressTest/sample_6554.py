club_members_premise = 30
club_members_hypothesis = 35

# the hypothesis refers to the number of club members who traveled to each country
if club_members_premise <= club_members_hypothesis:
    # check if the estimate of 'club_members_hypothesis' contradicts the number of club members reported in the premise
    label = "contradiction"
elif club_members_hypothesis - club_members_premise > 1:
    # check if the number of club members who traveled to each country in the hypothesis contradicts the number of club members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
