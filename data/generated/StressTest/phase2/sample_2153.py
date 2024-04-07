# Premise: After 30 minutes, Pat stops to stretch.
# Hypothesis: After more than 30 minutes, Pat stops to stretch.
# Golden Label: contradiction

pat_stops_premise = 30
pat_stops_hypothesis = 30

# the hypothesis talks about the time Pat stops to stretch, which is also mentioned in the premise
if pat_stops_hypothesis > pat_stops_premise:
    # check if the hypothesis value contradicts the 'pat_stops_premise'
    label = "contradiction"
elif pat_stops_hypothesis < pat_stops_premise:
    # check if the hypothesis value contradicts the 'pat_stops_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

