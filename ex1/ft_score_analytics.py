#!/usr/bin/python3.12

import sys

argc = len(sys.argv)
scores_list = []

print("=== Player Score Analytics ===")

for arg in sys.argv[1:]:
    try:
        score = int(arg)
        scores_list.append(score)

    except ValueError:
        print(f"Invalid parameter: '{arg}'")

total_valid_players = len(scores_list)
if len(scores_list) > 0:
    total_score = sum(scores_list)
    average_score = total_score / total_valid_players

    print(f"Scores processed: {scores_list}")
    print(f"Total players: {total_valid_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {max(scores_list)}")
    print(f"Low score: {min(scores_list)}")
    print(f"Score range: {max(scores_list) - min(scores_list)}\n")

else:
    print("No scores provided. "
          "Usage: python3 ft_score_analytics.py <score1> <score2> ...\n")
