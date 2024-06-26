hostages_beheaded_premise = 3
hostages_beheaded_hypothesis = 3
kidnapped_guardsmen_premise = 15
kidnapped_guardsmen_hypothesis = 15

# the hypothesis talks about the number of kidnapped Iraqi National Guard members, which is also mentioned in the premise
if hostages_beheaded_hypothesis!= hostages_beheaded_premise:
    # check if the number of beheaded hostages in the hypothesis contradicts the number of beheaded hostages from the premise
    label = "contradiction"
elif kidnapped_guardsmen_hypothesis!= kidnapped_guardsmen_premise:
    # check if the number of kidnapped guardsmen in the hypothesis contradicts the number of kidnapped guardsmen from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
