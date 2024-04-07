# Premise: It takes Jack and Lee respectively 6 and 10 minutes to finish each lap.
# Hypothesis: It takes Jack and Lee respectively more than 5 and 10 minutes to finish each lap.
# Golden Label: entailment

jack_time_premise = 6
lee_time_premise = 10
jack_time_hypothesis = 5
lee_time_hypothesis = 10

# the hypothesis talks about the time Jack and Lee take to finish each lap
if jack_time_premise <= jack_time_hypothesis:
    # check if Jack's time in the premise contradicts the hypothesis's estimate of more than 'jack_time_hypothesis'
    label = "contradiction"
elif lee_time_premise < lee_time_hypothesis:
    # check if Lee's time in the premise contradicts the hypothesis's estimate of more than 'lee_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

