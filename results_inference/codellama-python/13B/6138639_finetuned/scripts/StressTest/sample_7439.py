fastest_horses_premise = 3
fastest_horses_hypothesis = 4
total_horses = 25

# the hypothesis talks about the number of fastest horses the London Racetrack needs to submit to the Kentucky Derby, referenced also in the premise
if fastest_horses_hypothesis!= fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
