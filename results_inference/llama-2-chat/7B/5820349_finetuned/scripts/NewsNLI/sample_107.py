arrested_premise = 5
arrested_hypothesis = 5
officers_premise = 21
officers_hypothesis = 21
demonstrator_premise = 1
demonstrator_hypothesis = 1

# the hypothesis mentions the number of people arrested, which is also mentioned in the premise
# the hypothesis also mentions the number of hurt officers and demonstrators, which are also referenced in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of people arrested in the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
elif officers_hypothesis!= officers_premise:
    # check if the number of hurt officers from the hypothesis contradicts the number of hurt officers in the premise
    label = "contradiction"
elif demonstrator_hypothesis!= demonstrator_premise:
    # check if the number of hurt demonstrators from the hypothesis contradicts the number of hurt demonstrators in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
