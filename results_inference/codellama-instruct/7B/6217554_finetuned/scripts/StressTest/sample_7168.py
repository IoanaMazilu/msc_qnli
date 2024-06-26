people_premise = 1
people_between_premise = 7
people_after_premise = 20
people_between_hypothesis = 7
people_after_hypothesis = 20

# the hypothesis talks about the number of people who entered the theater between Sujit and Suraj and after Suraj
if people_between_hypothesis!= people_between_premise:
    # check if the number of people between Sujit and Suraj in the hypothesis contradicts the estimate of more than 'people_between_premise'
    label = "contradiction"
elif people_after_hypothesis!= people_after_premise:
    # check if the number of people after Suraj in the hypothesis contradicts the number of people after Suraj reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
