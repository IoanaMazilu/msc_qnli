club_members_premise = 30
club_members_france_premise = 26
club_members_italy_premise = 32

# the hypothesis refers to the number of members traveling to each country mentioned in the premise
if club_members_premise <= club_members_france_hypothesis:
    # check if the estimate of 'club_members_france_hypothesis' contradicts the number of members traveling to France in the premise
    label = "contradiction"
elif club_members_premise <= club_members_italy_hypothesis:
    # check if the estimate of 'club_members_italy_hypothesis' contradicts the number of members traveling to Italy in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
