premise_cookies_eaten_by_michael = 7/8
premise_cookies_eaten_by_steve = 1/2
premise_cookies_eaten_by_tyler = 150

hypothesis_cookies_eaten_by_michael = 1/8
hypothesis_cookies_eaten_by_steve = 1/2
hypothesis_cookies_eaten_by_tyler = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve, and Tyler
if hypothesis_cookies_eaten_by_michael!= premise_cookies_eaten_by_michael:
    # check if the hypothesis value contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif hypothesis_cookies_eaten_by_steve!= premise_cookies_eaten_by_steve:
    # check if the hypothesis value contradicts the number of cookies eaten by Steve in the premise
    label = "contradiction"
elif hypothesis_cookies_eaten_by_tyler!= premise_cookies_eaten_by_tyler:
    # check if the hypothesis value contradicts the number of cookies eaten by Tyler in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
