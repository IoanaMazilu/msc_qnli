hrs_premise = 1
hrs_hypothesis = 3
mph_premise = 46
mph_hypothesis = 46

# the hypothesis talks about the speed of Andrew's drive, which is also mentioned in the premise
if hrs_hypothesis <= hrs_premise:
    # check if the hypothesis value contradicts the estimate of 'hrs_premise'
    label = "contradiction"
elif mph_hypothesis!= mph_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
