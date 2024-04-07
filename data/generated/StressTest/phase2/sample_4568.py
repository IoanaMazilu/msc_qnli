# Premise: Ramzi walked for 3 days.
# Hypothesis: Ramzi walked for less than 3 days.
# Golden Label: contradiction

walking_days_premise = 3
walking_days_hypothesis = 3

# the hypothesis talks about the number of days Ramzi walked, mentioned also in the premise
if walking_days_hypothesis == walking_days_premise:
    # check if the hypothesis value contradicts the premise of walking less than 'walking_days_premise'
    label = "contradiction"
else:
    # the premise clearly states the number of walking days
    # any number of walking days less than 'walking_days_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

