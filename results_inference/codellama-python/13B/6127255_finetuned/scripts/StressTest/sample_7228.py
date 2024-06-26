# defining the marks obtained by Nancy in the premise and hypothesis
literature_premise = 86
literature_hypothesis = 66
history_premise = 75
history_hypothesis = 75
home_economics_premise = 52
home_economics_hypothesis = 52
physical_education_premise = 68
physical_education_hypothesis = 68
art_premise = 89
art_hypothesis = 89

# comparing the marks in the premise and hypothesis
if literature_hypothesis >= literature_premise:
    # check if the mark in literature in the hypothesis contradicts the premise of less than 86 marks
    label = "contradiction"
elif history_hypothesis!= history_premise or home_economics_hypothesis!= home_economics_premise or physical_education_hypothesis!= physical_education_premise or art_hypothesis!= art_premise:
    # check if the marks in other subjects in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the mark in literature
    # the marks in other subjects are exactly the same in the premise and hypothesis
    # so, any mark in literature less than 86 and the exact marks in other subjects are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)