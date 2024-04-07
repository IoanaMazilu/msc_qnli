# Premise: If Tim hires this freelancer, and hires him again to make alterations which took less than 80 more hours.
# Hypothesis: If Tim hires this freelancer, and hires him again to make alterations which took 20 more hours.
# Golden Label: neutral

alteration_hours_premise = 80
alteration_hours_hypothesis = 20

# the hypothesis talks about the hours of alterations, referenced also in the premise
if alteration_hours_hypothesis > alteration_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'alteration_hours_premise'
    label = "contradiction"
elif alteration_hours_hypothesis == alteration_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'alteration_hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the hours of alterations
    # any number of hours less than 'alteration_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

