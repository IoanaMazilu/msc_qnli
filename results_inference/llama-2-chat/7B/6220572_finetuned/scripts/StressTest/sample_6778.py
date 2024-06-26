bright_percentage_premise = 40
bright_percentage_hypothesis = 60
bivi_percentage_premise = 65
bivi_percentage_hypothesis = 65
lisa_percentage_premise = 45
lisa_percentage_hypothesis = 45

# the hypothesis refers to the percentages of Bright, Bivi and Lisa in the premise
if bright_percentage_hypothesis <= bright_percentage_premise:
    # check if the hypothesis value contradicts the percentage of Bright in the premise
    label = "contradiction"
elif bivi_percentage_hypothesis!= bivi_percentage_premise:
    # check if the percentage of Bivi in the hypothesis contradicts the percentage of Bivi reported in the premise
    label = "contradiction"
elif lisa_percentage_hypothesis!= lisa_percentage_premise:
    # check if the percentage of Lisa in the hypothesis contradicts the percentage of Lisa reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
