people_between_sujit_suraj = 7
people_after_suraj = 20
people_between_sujit_suraj_hypothesis = 8
people_after_suraj_hypothesis = 20

# the hypothesis talks about the number of people that entered the theater between Sujit and Suraj and after Suraj, which is also mentioned in the premise
if people_between_sujit_suraj_hypothesis!= people_between_sujit_suraj:
    label = "contradiction"
elif people_after_suraj_hypothesis!= people_after_suraj:
    label = "contradiction"
else:
    label = "neutral"

print(label)
