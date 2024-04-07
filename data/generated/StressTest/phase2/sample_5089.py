# Premise: When Sally went to the candy store, she bought less than 45 licorice sticks.
# Hypothesis: When Sally went to the candy store, she bought 25 licorice sticks.
# Golden Label: neutral

licorice_sticks_premise = 45
licorice_sticks_hypothesis = 25

# the hypothesis refers to the number of licorice sticks bought by Sally, mentioned also in the premise
if licorice_sticks_hypothesis >= licorice_sticks_premise:
    # check if the number of licorice sticks bought in the hypothesis contradicts the premise estimate of less than 'licorice_sticks_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the number of licorice sticks
    # any number of licorice sticks less than 'licorice_sticks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

