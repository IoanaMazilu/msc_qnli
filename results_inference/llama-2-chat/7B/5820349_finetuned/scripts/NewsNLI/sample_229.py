killed_premise = 1
killed_hypothesis = 6
wounded_premise = 1000
wounded_hypothesis = 1000

# the hypothesis mentions the number of people killed and wounded in demonstrations, which are also mentioned in the premise
if killed_hypothesis < killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
elif wounded_hypothesis < wounded_premise:
    # check if the number of people wounded from the hypothesis contradicts the number of people wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
