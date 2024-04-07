# Premise: A train leaves Jammu for Chennai exactly at 12 noon everyday of the week.
# Hypothesis: A train leaves Jammu for Chennai exactly at less than 42 noon everyday of the week.
# Golden Label: entailment

departure_time_premise = 12
departure_time_hypothesis = 42

# the hypothesis talks about the departure time of the train from Jammu for Chennai, which is also mentioned in the premise
if departure_time_hypothesis != departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis departure time does not contradict the premise departure time, we can infer entailment
    label = "entailment"

print(label)

