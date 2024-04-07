# Premise: If Sanket finishes the race by clocking 15 minutes, how far was Suresh from the finish line when Sam must have finished the race?
# Hypothesis: If Sanket finishes the race by clocking less than 35 minutes, how far was Suresh from the finish line when Sam must have finished the race?
# Golden Label: entailment

time_sanket_finishes_premise = 15
time_sanket_finishes_hypothesis = 35

# the hypothesis talks about the time Sanket finishes the race, referenced also in the premise
if time_sanket_finishes_hypothesis < time_sanket_finishes_premise:
    # check if the hypothesis value contradicts the premise's statement of Sanket's finish time
    label = "contradiction"
elif time_sanket_finishes_premise != time_sanket_finishes_hypothesis:
    # check if the hypothesis value differs from the premise's statement of Sanket's finish time
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict and do not differ from the premise ones, we can infer entailment
    label = "entailment"

print(label)

