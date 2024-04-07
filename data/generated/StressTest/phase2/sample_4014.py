# Premise: If Leo gains 10 pounds, he will weigh 50% more than his sister Kendra.
# Hypothesis: If Leo gains less than 60 pounds, he will weigh 50% more than his sister Kendra.
# Golden Label: entailment

leo_gain_premise = 10
leo_gain_hypothesis = 60
percentage_difference = 50

# the hypothesis gives a different estimate of Leo's weight gain compared to the premise
if leo_gain_hypothesis <= leo_gain_premise:
    # check if the hypothesis value contradicts the estimate of 'leo_gain_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Leo's weight gain
    # any weight gain greater than 'leo_gain_premise' and less than 'leo_gain_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

