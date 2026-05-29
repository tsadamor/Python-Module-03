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
if len(scores_list) > 0:
    print(f"Scores processed: {scores_list}")
    print(f"Total players: {argc - 1}")
    print(f"Total score: {sum(scores_list)}")
    print(f"Average score: {(sum(scores_list) / argc - 1):.1f}")
    print(f"High score: {max(scores_list)}")
    print(f"Low score: {min(scores_list)}")
    print(f"Score range: {max(scores_list) - min(scores_list)}")

else:
    print("No scores provided. "
          "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
