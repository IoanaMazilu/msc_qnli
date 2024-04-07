# Premise: If the three started to fish together and after 40 minutes Mike and Bob left, how many fish did the three fishermen catch in one hour?
# Hypothesis: If the three started to fish together and after more than 40 minutes Mike and Bob left, how many fish did the three fishermen catch in one hour?
# Golden Label: contradiction

fishing_time_premise = 40
fishing_time_hypothesis = 40

# The hypothesis talks about the time Mike and Bob left, which is also referenced in the premise
if fishing_time_hypothesis > fishing_time_premise:
    # check if the hypothesis value contradicts the stated 'fishing_time_premise'
    label = "contradiction"
else:
    # the premise gives an exact time for when Mike and Bob left
    # the same exact time stated in the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)

