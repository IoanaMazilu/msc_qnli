less_than_500_seniors_premise = 500
less_than_500_seniors_hypothesis = 300
percentage_cars_premise = 50
percentage_cars_hypothesis = 50

# the hypothesis talks about the number of seniors and the percentage of cars they have, referenced also in the premise
if less_than_500_seniors_hypothesis >= less_than_500_seniors_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_500_seniors_premise'
    label = "contradiction"
elif percentage_cars_hypothesis!= percentage_cars_premise:
    # check if the percentage of cars in the hypothesis contradicts the percentage of cars reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of seniors
    # any number of seniors less than 'less_than_500_seniors_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)