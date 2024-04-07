def rank_obeya_score(score):
    # OBEYA スコアに基づいてランク付けを行う関数
    if score > 200:
        return '[OBEYA]'
    elif score > 150:
        return '[MESSY]'
    else:
        return '[CLEAN]'
