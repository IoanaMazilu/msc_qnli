 roses_initial_premise = 37.0
 roses_sold_premise = 16.0
 roses_picked_premise = 19.0
 roses_hypothesis = 40.0

 # the hypothesis refers to the number of roses, which are also mentioned in the premise
 # compute the total number of roses in the premise
 roses_total_premise = roses_initial_premise - roses_sold_premise + roses_picked_premise
 if roses_hypothesis!= roses_total_premise:
     # check if the number of roses in the hypothesis contradicts the number of roses from the premise
     label = "contradiction"
 else:
     # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
     label = "entailment"    

 print(label)
 #