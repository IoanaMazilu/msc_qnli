# defining the scores in the premise and hypothesis
french_premise = 46
french_hypothesis = 86
geography_premise = 75
geography_hypothesis = 75
art_design_premise = 72
art_design_hypothesis = 72
history_premise = 63
history_hypothesis = 63
physical_education_premise = 65
physical_education_hypothesis = 65

# the hypothesis refers to the scores in the premise
if french_hypothesis <= french_premise:
    # check if the French score in the hypothesis contradicts the estimate of more than 'french_premise'
    label = "contradiction"
elif geography_hypothesis!= geography_premise or art_design_hypothesis!= art_design_premise or history_hypothesis!= history_premise or physical_education_hypothesis!= physical_education_premise:
    # check if the other scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the French score
    # any French score greater than 'french_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
