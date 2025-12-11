# page_replacement.py

def simulate_fifo(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []

    queue_index = 0  # to track which frame to replace

    for page in pages:
        step_info = {}
        if page in frames:
            hits += 1
            hit_or_miss = "Hit"
        else:
            page_faults += 1
            hit_or_miss = "Miss"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # replace in FIFO manner
                frames[queue_index] = page
                queue_index = (queue_index + 1) % frame_count

        step_info["page"] = page
        step_info["frames"] = frames.copy()
        step_info["result"] = hit_or_miss
        steps.append(step_info)

    total_access = len(pages)
    hit_ratio = hits / total_access if total_access > 0 else 0

    return {
        "name": "FIFO",
        "steps": steps,
        "page_faults": page_faults,
        "hits": hits,
        "hit_ratio": hit_ratio
    }


def simulate_lru(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []

    # to track last used index of each page in frames
    last_used = {}

    for current_index, page in enumerate(pages):
        step_info = {}

        if page in frames:
            hits += 1
            hit_or_miss = "Hit"
        else:
            page_faults += 1
            hit_or_miss = "Miss"

            if len(frames) < frame_count:
                frames.append(page)
            else:
                # find least recently used page
                # check last_used index for each page in frames
                lru_page = None
                lru_index = float("inf")

                for p in frames:
                    # if never used before, treat as very old
                    idx = last_used.get(p, -1)
                    if idx < lru_index:
                        lru_index = idx
                        lru_page = p

                # replace lru_page with current page
                replace_index = frames.index(lru_page)
                frames[replace_index] = page

        # update last used index of current page
        last_used[page] = current_index

        step_info["page"] = page
        step_info["frames"] = frames.copy()
        step_info["result"] = hit_or_miss
        steps.append(step_info)

    total_access = len(pages)
    hit_ratio = hits / total_access if total_access > 0 else 0

    return {
        "name": "LRU",
        "steps": steps,
        "page_faults": page_faults,
        "hits": hits,
        "hit_ratio": hit_ratio
    }


def simulate_optimal(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []

    for i, page in enumerate(pages):
        step_info = {}

        if page in frames:
            hits += 1
            hit_or_miss = "Hit"
        else:
            page_faults += 1
            hit_or_miss = "Miss"

            if len(frames) < frame_count:
                frames.append(page)
            else:
                # find page to replace using optimal strategy
                farthest_index = -1
                page_to_replace = None

                for p in frames:
                    # check when this page will appear next
                    try:
                        next_use = pages.index(p, i + 1)
                    except ValueError:
                        # page not used again, best to replace this
                        next_use = float("inf")

                    if next_use > farthest_index:
                        farthest_index = next_use
                        page_to_replace = p

                replace_index = frames.index(page_to_replace)
                frames[replace_index] = page

        step_info["page"] = page
        step_info["frames"] = frames.copy()
        step_info["result"] = hit_or_miss
        steps.append(step_info)

    total_access = len(pages)
    hit_ratio = hits / total_access if total_access > 0 else 0

    return {
        "name": "Optimal",
        "steps": steps,
        "page_faults": page_faults,
        "hits": hits,
        "hit_ratio": hit_ratio
    }


def print_result(result):
    print(f"\nAlgorithm: {result['name']}")
    print("Step\tPage\tFrames\t\tResult")
    for idx, step in enumerate(result["steps"], start=1):
        frames_str = " ".join(str(x) for x in step["frames"])
        print(f"{idx}\t{step['page']}\t{frames_str:<10}\t{step['result']}")
    print(f"Total Page Faults: {result['page_faults']}")
    print(f"Total Hits: {result['hits']}")
    print(f"Hit Ratio: {result['hit_ratio']*100:.2f}%")
    

def main():
    print("Efficient Page Replacement Algorithm Simulator")
    frame_count = int(input("Enter number of frames: "))
    ref_string = input("Enter reference string (space-separated pages): ")
    pages = list(map(int, ref_string.split()))

    fifo_result = simulate_fifo(pages, frame_count)
    lru_result = simulate_lru(pages, frame_count)
    optimal_result = simulate_optimal(pages, frame_count)

    print_result(fifo_result)
    print_result(lru_result)
    print_result(optimal_result)

    # simple comparison
    all_results = [fifo_result, lru_result, optimal_result]
    best = min(all_results, key=lambda r: r["page_faults"])
    print(f"\nBest algorithm for this input (least page faults): {best['name']}")


if __name__ == "__main__":
    main()
