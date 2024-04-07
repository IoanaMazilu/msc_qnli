# Premise: A train leaves Jammu for Chennai exactly at 12 noon everyday of the week.
# Hypothesis: A train leaves Jammu for Chennai exactly at 62 noon everyday of the week.
# Golden Label: contradiction

departure_time_premise = 12
departure_time_hypothesis = 62

# the hypothesis refers to the departure time of a train mentioned in the premise
if departure_time_hypothesis != departure_time_premise:
    # check if the departure time in the hypothesis contradicts the departure time reported in the premise
    label = "contradiction"
else:
    # if the departure time in the hypothesis does not contradict the departure time in the premise, we can infer entailment
    label = "entailment"

print(label)

