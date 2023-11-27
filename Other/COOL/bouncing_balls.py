def bouncing_ball(h, bounce, window):
    count = -1
    while h * bounce > window and 0 < bounce < 1 and h > 0:
        if count == -1:
            count = count + 2
        count = count + 2
        h = h * bounce
    if h * bounce == window:
        count = count + 2
    return count

