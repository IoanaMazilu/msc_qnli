 fish_premise = 49.0
 fish_received_premise = 18.0
 marbles_hypothesis = 67.0

 # the hypothesis refers to the number of marbles, which can be calculated from the number of fish in the premise
 # compute the total number of marbles in the premise
 total_marbles_premise = (fish_premise + fish_received_premise) * 2
 if marbles_hypothesis!= total_marbles_premise:
     # check if the number of marbles in the hypothesis contradicts the number of marbles calculated from the premise
     label = "contradiction"
 else:
     # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
     label = "entailment"    

 print(label)
 #