police_officers_premise = 21
police_officers_hypothesis = 21
demonstrator_premise = 1
demonstrator_hypothesis = 1
arrested_premise = 5
arrested_hypothesis = 5

# the hypothesis mentions the number of arrested people, which is also mentioned in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of arrested people in the hypothesis contradicts the number of arrested people in the premise
    label = "contradiction"
elif police_officers_hypothesis!= police_officers_premise:
    # check if the number of police officers in the hypothesis contradicts the number of police officers in the premise
    label = "contradiction"
elif demonstrator_hypothesis!= demonstrator_premise:
    # check if the number of demonstrators in the hypothesis contradicts the number of demonstrators in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
