import pandas as pd

def calculate_form_score(placements, field_sizes):
    scores = [1 - (p / f) for p, f in zip(placements, field_sizes)]
    return sum(scores) / len(scores)

def calculate_popularity(odds_list):
    odds_scores = [1 / o for o in odds_list]
    min_score = min(odds_scores)
    max_score = max(odds_scores)
    if max_score == min_score:
        return [1.0] * len(odds_scores)
    return [(x - min_score) / (max_score - min_score) for x in odds_scores]

def estimate_win_probabilities(df):
    df["熱門程度"] = calculate_popularity(df["賠率"].tolist())
    df["form_score"] = df.apply(lambda row: calculate_form_score(
        [int(x) for x in row["近五場名次"].split()],
        [int(x) for x in row["近五場出馬數"].split()]
    ), axis=1)
    df["勝率分數"] = (
        0.4 * df["form_score"] +
        0.3 * df["騎師勝率"] +
        0.2 * df["練馬師勝率"] +
        0.1 * df["熱門程度"]
    )
    df["估計勝率"] = df["勝率分數"] / df["勝率分數"].sum()
    return df[["馬名", "估計勝率"]].sort_values(by="估計勝率", ascending=False)