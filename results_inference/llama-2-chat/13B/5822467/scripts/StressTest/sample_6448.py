john_age_premise = 8
john_age_hypothesis = 5
frank_age_premise = 0
frank_age_hypothesis = 0

# the premise refers to John's age in relation to Frank's age
if john_age_premise <= john_age_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif frank_age_hypothesis!= frank_age_premise:
    # check if the number of Frank's age in the hypothesis contradicts the number of Frank's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
