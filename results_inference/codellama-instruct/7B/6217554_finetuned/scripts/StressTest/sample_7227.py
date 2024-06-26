# define variables for each mark obtained in each subject
mark_al_premise = 66
mark_al_hypothesis = 86
mark_history_premise = 75
mark_history_hypothesis = 75
mark_he_premise = 52
mark_he_hypothesis = 52
mark_pe_premise = 68
mark_pe_hypothesis = 68
mark_art_premise = 89
mark_art_hypothesis = 89

# check if the marks obtained in each subject in the hypothesis contradict the ones reported in the premise
if mark_al_hypothesis >= mark_al_premise:
    label = "contradiction"
elif mark_history_hypothesis!= mark_history_premise:
    label = "contradiction"
elif mark_he_hypothesis!= mark_he_premise:
    label = "contradiction"
elif mark_pe_hypothesis!= mark_pe_premise:
    label = "contradiction"
elif mark_art_hypothesis!= mark_art_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
