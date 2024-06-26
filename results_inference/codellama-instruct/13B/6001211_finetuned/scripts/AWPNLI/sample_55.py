total_gems_premise = 5155.0
diamond_gems_premise = 45.0
ruby_gems_hypothesis = 5108.0

# the hypothesis refers to the number of ruby gems, which are also mentioned in the premise
# compute the total number of ruby gems in the premise
ruby_gems_premise = total_gems_premise - diamond_gems_premise
if ruby_gems_hypothesis!= ruby_gems_premise:
    # check if the number of ruby gems in the hypothesis contradicts the number of ruby gems from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
