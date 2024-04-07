# Premise: At the same time Joyce gets on an elevator on the 61 st floor of the same building and rides down at a rate of 78 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the less than 81 st floor of the same building and rides down at a rate of 78 floors per minute.
# Golden Label: entailment

joyce_floor_premise = 61
joyce_floor_hypothesis = 81
joyce_rate_premise = 78
joyce_rate_hypothesis = 78

# the hypothesis talks about the floor where Joyce starts in the elevator and the rate at which she rides down, referenced also in the premise
if joyce_floor_premise > joyce_floor_hypothesis:
    # check if the floor from where Joyce starts in the premise contradicts the estimate of less than 'joyce_floor_hypothesis'
    label = "contradiction"
elif joyce_rate_premise != joyce_rate_hypothesis:
    # check if the rate at which Joyce rides down in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact floor number and rate, both of which are consistent with the hypothesis
    label = "entailment"

print(label)

