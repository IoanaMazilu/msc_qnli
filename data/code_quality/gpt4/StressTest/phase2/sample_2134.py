england_france_premise = 0
england_france_hypothesis = 0
england_italy_premise = 7
england_italy_hypothesis = 6
france_italy_premise = 12
france_italy_hypothesis = 12

# the hypothesis refers to the number of club members that traveled to different countries pairs mentioned in the premise
if england_france_premise != england_france_hypothesis:
    # check if the hypothesis value for 'england_france_hypothesis' contradicts the premise
    label = "contradiction"
elif england_italy_premise <= england_italy_hypothesis:
    # check if the hypothesis value for 'england_italy_hypothesis' contradicts the premise
    label = "contradiction"
elif france_italy_premise != france_italy_hypothesis:
    # check if the hypothesis value for 'france_italy_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
