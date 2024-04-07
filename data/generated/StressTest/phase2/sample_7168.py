# Premise: more than 1 people entered the theater between Sujit and Suraj and 20 people entered the theater after Suraj.
# Hypothesis: 7 people entered the theater between Sujit and Suraj and 20 people entered the theater after Suraj.
# Golden Label: neutral

people_between_sujit_suraj_premise = 1
people_between_sujit_suraj_hypothesis = 7
people_after_suraj_premise = 20
people_after_suraj_hypothesis = 20

# the hypothesis refers to the number of people entering the theater mentioned in the premise
if people_between_sujit_suraj_hypothesis <= people_between_sujit_suraj_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_between_sujit_suraj_premise'
    label = "contradiction"
elif people_after_suraj_hypothesis != people_after_suraj_premise:
    # check if the number of people entering the theater after Suraj in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people entering the theater between Sujit and Suraj
    # any number of people greater than 'people_between_sujit_suraj_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

