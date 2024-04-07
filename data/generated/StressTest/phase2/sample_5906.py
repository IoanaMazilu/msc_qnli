# Premise: Michael ate 1/8 of the cookies, Steve ate one half and Tyler ate 150 more cookies than Michael.
# Hypothesis: Michael ate more than 1/8 of the cookies, Steve ate one half and Tyler ate 150 more cookies than Michael.
# Golden Label: contradiction

cookies_eaten_michael_premise = 1/8
cookies_eaten_michael_hypothesis = 1/8
cookies_eaten_steve_premise = 1/2
cookies_eaten_steve_hypothesis = 1/2
cookies_eaten_tyler_premise = cookies_eaten_michael_premise + 150
cookies_eaten_tyler_hypothesis = cookies_eaten_michael_hypothesis + 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler, which is also mentioned in the premise
if cookies_eaten_michael_hypothesis <= cookies_eaten_michael_premise:
    # check if the hypothesis value contradicts the estimate in the premise regarding the number of cookies eaten by Michael
    label = "contradiction"
elif cookies_eaten_steve_hypothesis != cookies_eaten_steve_premise or cookies_eaten_tyler_hypothesis != cookies_eaten_tyler_premise:
    # check if the number of cookies eaten by Steve or Tyler in the hypothesis contradicts the number of cookies they ate according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

