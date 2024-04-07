# Premise: If Abhay double his speed, then he would take 1 hour less than Sammer.
# Hypothesis: If Abhay double his speed, then he would take less than 5 hour less than Sammer.
# Golden Label: entailment

time_difference_premise = 1
time_difference_hypothesis = 5

# the hypothesis talks about the time difference between Abhay and Sammer when Abhay doubles his speed, which is also mentioned in the premise
if time_difference_hypothesis < time_difference_premise:
    # check if the hypothesis value contradicts the estimate of 'time_difference_premise'
    label = "contradiction"
elif time_difference_hypothesis > time_difference_premise:
    # the premise gives a specific time difference
    # any time difference greater than 'time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and premise value are equal, we can infer entailment
    label = "entailment"

print(label)

