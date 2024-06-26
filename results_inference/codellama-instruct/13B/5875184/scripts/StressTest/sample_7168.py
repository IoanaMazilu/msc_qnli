premise_people_entered_theater_between_sujit_and_suraj = 1
premise_people_entered_theater_after_suraj = 20
hypothesis_people_entered_theater_between_sujit_and_suraj = 7
hypothesis_people_entered_theater_after_suraj = 20

# the hypothesis refers to the number of people who entered the theater between Sujit and Suraj and after Suraj
if hypothesis_people_entered_theater_between_sujit_and_suraj <= premise_people_entered_theater_between_sujit_and_suraj:
    # check if the estimate of 'hypothesis_people_entered_theater_between_sujit_and_suraj' contradicts the number of people who entered the theater between Sujit and Suraj in the premise
    label = "contradiction"
elif hypothesis_people_entered_theater_after_suraj!= premise_people_entered_theater_after_suraj:
    # check if the number of people who entered the theater after Suraj in the hypothesis contradicts the number of people who entered the theater after Suraj reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
