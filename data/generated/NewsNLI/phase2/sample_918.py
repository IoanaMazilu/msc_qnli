# Premise: Victory at Wimbledon will give Nadal his 11th grand slam title and close on the record 16 of arch-rival and third seed Roger Federer, but again the world No.
# Hypothesis: Nadal won three grand slams including Wimbledon where he defends the title.
# Golden Label: neutral

nadal_grand_slam_titles_premise = 11
nadal_grand_slam_titles_hypothesis = 3

# the hypothesis states the number of grand slams won by Nadal, which is also mentioned in the premise
# however, the hypothesis indicates that Nadal has won 3 grand slams, including Wimbledon, while the premise states that he will win his 11th grand slam title if he wins Wimbledon
if nadal_grand_slam_titles_hypothesis != nadal_grand_slam_titles_premise:
    # check if the number of grand slams won by Nadal in the hypothesis contradicts the number of grand slams mentioned in the premise
    label = "contradiction"
else:
    # if the number of grand slams won by Nadal in the hypothesis does not contradict the number of grand slams mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

