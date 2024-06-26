french_language_premise = 46
french_language_hypothesis = 86
geography_premise = 75
geography_hypothesis = 75
art_design_premise = 72
art_design_hypothesis = 72
history_premise = 63
history_hypothesis = 63
physical_education_premise = 65
physical_education_hypothesis = 65

# the hypothesis talks about the marks of Adam in different subjects, referenced also in the premise
if french_language_hypothesis <= french_language_premise:
    # check if the hypothesis value contradicts the estimate of more than 'french_language_premise'
    label = "contradiction"
elif geography_hypothesis!= geography_premise:
    # check if the geography score in the hypothesis contradicts the geography score reported in the premise
    label = "contradiction"
elif art_design_hypothesis!= art_design_premise:
    # check if the art and design score in the hypothesis contradicts the art and design score reported in the premise
    label = "contradiction"
elif history_hypothesis!= history_premise:
    # check if the history score in the hypothesis contradicts the history score reported in the premise
    label = "contradiction"
elif physical_education_hypothesis!= physical_education_premise:
    # check if the physical education score in the hypothesis contradicts the physical education score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark of Adam
    # any average mark greater than 'french_language_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
