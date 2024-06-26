people_premise = 60
people_hypothesis = 20
iceland_visits_premise = 35
iceland_visits_hypothesis = 35
norway_visits_premise = 23
norway_visits_hypothesis = 23

# the hypothesis refers to the number of people and the number of visits to Iceland and Norway mentioned in the premise
if people_premise <= people_hypothesis:
    # check if the estimate of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif iceland_visits_hypothesis!= iceland_visits_premise or norway_visits_hypothesis!= norway_visits_premise:
    # check if the number of visits to Iceland and Norway in the hypothesis contradicts the number of visits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
