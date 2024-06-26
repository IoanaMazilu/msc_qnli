boys_premise = 6
girls_premise = 4
hypothesis_boys = <6
hypothesis_girls = <4

# the hypothesis talks about the number of boys and girls in a group, referenced also in the premise
if hypothesis_boys <= boys_premise:
    # check if the hypothesis value contradicts the estimate of 'boys_premise'
    label = "contradiction"
elif hypothesis_girls <= girls_premise:
    # check if the hypothesis value contradicts the estimate of 'girls_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
