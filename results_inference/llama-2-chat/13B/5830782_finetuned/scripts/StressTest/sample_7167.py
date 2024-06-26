people_between_premise = 7
people_between_hypothesis = 1
people_after_premise = 20
people_after_hypothesis = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj, as mentioned in the premise
if people_between_hypothesis >= people_between_premise:
    # check if the hypothesis value contradicts the exact number of people who entered the theater between Sujit and Suraj as reported in the premise
    label = "contradiction"
elif people_after_hypothesis!= people_after_premise:
    # check if the number of people who entered the theater after Suraj in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
