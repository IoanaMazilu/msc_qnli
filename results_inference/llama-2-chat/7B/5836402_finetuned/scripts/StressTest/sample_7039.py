geography_history_government_average_premise = 26
history_average_premise = 60
government_average_premise = 72
art_average_premise = 85
literature_average_premise = 80

computer_science_average_hypothesis = 56
geography_history_government_average_hypothesis = 60
art_average_hypothesis = 72
literature_average_hypothesis = 80

# the hypothesis refers to the average marks of a student in the same subjects as the premise
if computer_science_average_hypothesis!= computer_science_average_premise:
    # check if the average marks of the computer science subject in the hypothesis contradicts the average marks of the same subject in the premise
    label = "contradiction"
elif geography_history_government_average_hypothesis!= geography_history_government_average_premise:
    # check if the average marks of the geography, history and government subjects in the hypothesis contradicts the average marks of the same subjects in the premise
    label = "contradiction"
elif art_average_hypothesis!= art_average_premise:
    # check if the average marks of the art subject in the hypothesis contradicts the average marks of the same subject in the premise
    label = "contradiction"
elif literature_average_hypothesis!= literature_average_premise:
    # check if the average marks of the literature subject in the hypothesis contradicts the average marks of the same subject in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
