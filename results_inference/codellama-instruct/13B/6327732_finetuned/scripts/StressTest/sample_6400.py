premise_miami = 8/2
premise_kennedy = 1
premise_logan = 4

hypothesis_miami = 1/2
hypothesis_kennedy = 1
hypothesis_logan = 4

# the hypothesis refers to the number of passengers that used Miami Airport and the number that used Kennedy Airport, which are also mentioned in the premise
if hypothesis_miami!= premise_miami or hypothesis_kennedy!= premise_kennedy:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif hypothesis_logan!= premise_logan:
    # check if the hypothesis value for the number of passengers that used Logan Airport contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
