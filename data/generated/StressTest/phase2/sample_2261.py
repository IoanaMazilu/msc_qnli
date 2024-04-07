# Premise: Jason is 4 times older than Bob at present.
# Hypothesis: Jason is 5 times older than Bob at present.
# Golden Label: contradiction

jason_age_times_bob_premise = 4
jason_age_times_bob_hypothesis = 5

# the hypothesis refers to the age difference between Jason and Bob, mentioned in the premise
if jason_age_times_bob_premise != jason_age_times_bob_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis age differences match
    label = "entailment"

print(label)

