cleaning_time_premise = 3
cleaning_time_hypothesis = 3

# the hypothesis talks about the time it would take to clean the house if Anne's speed was doubled, which is also referenced in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is entailed by the premise
    label = "entailment"

print(label)
