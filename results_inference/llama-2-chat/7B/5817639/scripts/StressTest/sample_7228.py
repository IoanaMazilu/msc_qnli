american_literature_marks_premise = 86
american_literature_marks_hypothesis = 66
history_marks_premise = 75
history_marks_hypothesis = 75
home_economics_marks_premise = 52
home_economics_marks_hypothesis = 52
physical_education_marks_premise = 68
physical_education_marks_hypothesis = 68
art_marks_premise = 89
art_marks_hypothesis = 89

# the hypothesis talks about the marks obtained by Nancy in 6 subjects
if american_literature_marks_hypothesis <= american_literature_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'american_literature_marks_premise'
    label = "contradiction"
elif history_marks_hypothesis!= history_marks_premise:
    # check if the number of marks in History in the hypothesis contradicts the number of marks in History reported in the premise
    label = "contradiction"
elif home_economics_marks_hypothesis!= home_economics_marks_premise:
    # check if the number of marks in Home Economics in the hypothesis contradicts the number of marks in Home Economics reported in the premise
    label = "contradiction"
elif physical_education_marks_hypothesis!= physical_education_marks_premise:
    # check if the number of marks in Physical Education in the hypothesis contradicts the number of marks in Physical Education reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
