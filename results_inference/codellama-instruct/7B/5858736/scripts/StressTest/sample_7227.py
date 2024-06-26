marks_American_Literature_premise = 66
marks_American_Literature_hypothesis = 86
marks_History_premise = 75
marks_History_hypothesis = 75
marks_Home_Economics_premise = 52
marks_Home_Economics_hypothesis = 52
marks_Physical_Education_premise = 68
marks_Physical_Education_hypothesis = 68
marks_Art_premise = 89
marks_Art_hypothesis = 89

# the hypothesis talks about the number of marks obtained in each subject, referenced also in the premise
if marks_American_Literature_hypothesis >= marks_American_Literature_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_American_Literature_premise'
    label = "contradiction"
elif marks_History_hypothesis >= marks_History_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_History_premise'
    label = "contradiction"
elif marks_Home_Economics_hypothesis >= marks_Home_Economics_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_Home_Economics_premise'
    label = "contradiction"
elif marks_Physical_Education_hypothesis >= marks_Physical_Education_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_Physical_Education_premise'
    label = "contradiction"
elif marks_Art_hypothesis >= marks_Art_premise:
    # check if the hypothesis value contradicts the estimate of less than'marks_Art_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
