# defining the marks Nancy obtained in each subject according to the premise
american_literature_mark_premise = 66
history_mark_premise = 75
home_economics_mark_premise = 52
physical_education_mark_premise = 68
art_mark_premise = 89

# defining the marks Nancy obtained in each subject according to the hypothesis
american_literature_mark_hypothesis = 86
history_mark_hypothesis = 75
home_economics_mark_hypothesis = 52
physical_education_mark_hypothesis = 68
art_mark_hypothesis = 89

# comparing the marks Nancy obtained in each subject according to the premise and the hypothesis
if american_literature_mark_premise > american_literature_mark_hypothesis or \
   history_mark_premise > history_mark_hypothesis or \
   home_economics_mark_premise > home_economics_mark_hypothesis or \
   physical_education_mark_premise > physical_education_mark_hypothesis or \
   art_mark_premise > art_mark_hypothesis:
    # if the marks Nancy obtained in any subject according to the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the marks Nancy obtained in all subjects according to the hypothesis do not contradict the marks reported in the premise
    # but cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
