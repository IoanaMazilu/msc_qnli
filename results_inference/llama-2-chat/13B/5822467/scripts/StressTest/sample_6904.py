total_premise = less than 360
total_hypothesis = 160

# the hypothesis refers to the total amount paid to rent the tool, mentioned in the premise
if total_premise <= total_hypothesis:
    # check if the estimate of 'total_hypothesis' contradicts the total amount paid in the premise
    label = "contradiction"
elif total_hypothesis!= total_premise:
    # check if the total amount paid in the hypothesis contradicts the total amount paid reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
