def gen_containers(n):
    return ((w, h) for w in range(1, n+1) for h in range(1, w+1))

def gen_sub_rectangle_sizes(width, height):
    return ((w, h) for w in range(1, width+1) for h in range(1, height+1))

def num_contained_rects(container_width, container_height, rect_width, rect_height):
    return (container_width - rect_width + 1) * (container_height - rect_height + 1)

best = None
for container in gen_containers(100):
    num_rects = sum([num_contained_rects(*container, *rect) for rect in gen_sub_rectangle_sizes(*container)])
    if best is None or abs(2_000_000 - num_rects) < abs(2_000_000 - best[1]):
        print("Found new best", container)
        best = (container, num_rects)

best_rect = best[0]
print(best_rect[0] * best_rect[1])
