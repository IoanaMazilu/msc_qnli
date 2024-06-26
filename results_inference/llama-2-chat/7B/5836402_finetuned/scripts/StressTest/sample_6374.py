pencils_shreehari_premise = 125
pencils_shreehari_hypothesis = 525

# the hypothesis talks about the number of pencils Shreehari has, which is also mentioned in the premise
if pencils_shreehari_hypothesis!= pencils_shreehari_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
