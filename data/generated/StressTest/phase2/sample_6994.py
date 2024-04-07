# Premise: If this new machine can pick more than 10 apples every 30 minutes and Tim wants to pick 500 apples today.
# Hypothesis: If this new machine can pick 20 apples every 30 minutes and Tim wants to pick 500 apples today.
# Golden Label: neutral

apples_picked_premise = 10
apples_picked_hypothesis = 20
apples_goal = 500

# the hypothesis talks about the number of apples picked by the machine every 30 minutes, referenced also in the premise

if apples_picked_hypothesis <= apples_picked_premise:
    # check if the hypothesis value contradicts the estimate of more than 'apples_picked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples picked
    # any number of apples greater than 'apples_picked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

