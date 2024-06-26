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

# the hypothesis talks about the marks obtained by Nancy in different subjects, referenced also in the premise
if literature_hypothesis >= literature_premise:
    # check if the hypothesis value contradicts the estimate of less than 'literature_premise'
    label = "contradiction"
elif history_hypothesis!= history_premise:
    # check if the marks in History in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif home_economics_hypothesis!= home_economics_premise:
    # check if the marks in Home Economics in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif physical_education_hypothesis!= physical_education_premise:
    # check if the marks in Physical Education in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
elif art_hypothesis!= art_premise:
    # check if the marks in Art in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained by Nancy
    # any marks equal to the ones in the hypothesis are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
