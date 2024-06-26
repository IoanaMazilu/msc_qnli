deaths_germany_premise = 15
deaths_sweden_premise = 1
total_deaths_premise = deaths_germany_premise + deaths_sweden_premise

total_deaths_hypothesis = 16
deaths_sweden_hypothesis = 1

# the hypothesis mentions the total number of deaths and the number of deaths in Sweden, which are also mentioned in the premise
if total_deaths_hypothesis != total_deaths_premise:
    # check if the total number of deaths in the hypothesis contradicts the total number of deaths reported in the premise
    label = "contradiction"
elif deaths_sweden_hypothesis != deaths_sweden_premise:
    # check if the number of deaths in Sweden from the hypothesis contradicts the number of deaths in Sweden in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
