# Premise: If Yolanda's walking rate was more than 2 miles per hour and Bob т's was 4 miles per hour, how many miles had Bob walked when they met?
# Hypothesis: If Yolanda's walking rate was 3 miles per hour and Bob т's was 4 miles per hour, how many miles had Bob walked when they met?
# Golden Label: neutral

walking_rate_yolanda_premise = 2
walking_rate_yolanda_hypothesis = 3
walking_rate_bob_premise = 4
walking_rate_bob_hypothesis = 4

# the hypothesis talks about the walking rate of Yolanda and Bob, which is also referenced in the premise
if walking_rate_yolanda_hypothesis <= walking_rate_yolanda_premise:
    # check if the hypothesis value contradicts the estimate of more than 'walking_rate_yolanda_premise'
    label = "contradiction"
elif walking_rate_bob_hypothesis != walking_rate_bob_premise:
    # check if the walking rate of Bob in the hypothesis contradicts the walking rate of Bob reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking rate of Yolanda
    # any walking rate for Yolanda greater than 'walking_rate_yolanda_premise' is consistent with the premise, but can't be explicitly entailed from the premise
    label = "neutral"

print(label)

