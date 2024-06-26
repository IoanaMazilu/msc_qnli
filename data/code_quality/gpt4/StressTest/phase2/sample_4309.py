total_people_premise = 800
total_people_hypothesis = 100
graduated_k_premise = 40
graduated_k_hypothesis = 40
graduated_y_premise = 65
graduated_y_hypothesis = 65
live_z_premise = 30
live_z_hypothesis = 30

# the hypothesis talks about the number of people in a group, and their graduates or city of living
# the premise also gives information about a group of people and their graduates or city of living
if total_people_hypothesis >= total_people_premise:
    # check if the total number of people in the hypothesis contradicts the estimate of less than 'total_people_premise'
    label = "contradiction"
elif graduated_k_hypothesis != graduated_k_premise or graduated_y_hypothesis != graduated_y_premise or live_z_hypothesis != live_z_premise:
    # check if the number of people graduated from K, Y or live in Z, contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of people
    # any number of people less than 'total_people_premise' and the same number of people as graduates or residents does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
