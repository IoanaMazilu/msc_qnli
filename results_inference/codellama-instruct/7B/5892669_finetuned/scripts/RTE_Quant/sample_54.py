exports_rise_percentage_premise = 12.8
exports_rise_percentage_hypothesis = 10.5

# the hypothesis talks about the rise percentage of US exports, which is also mentioned in the premise
if exports_rise_percentage_hypothesis!= exports_rise_percentage_premise:
    # check if the rise percentage of exports in the hypothesis contradicts the rise percentage from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
