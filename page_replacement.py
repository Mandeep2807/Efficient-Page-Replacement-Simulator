# Efficient Page Replacement Algorithm Simulator
# This file contains full implementations of FIFO, LRU, and Optimal algorithms.
# Output includes page faults, hits, hit ratio, step-by-step frames, and a console display.

# -------------------------------------------------------------
# FIFO Algorithm (First-In-First-Out)
# Replaces the oldest loaded page in memory.
# -------------------------------------------------------------
def simulate_fifo(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []
    queue_index = 0  # Pointer for FIFO replacement

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
                # Replace using FIFO order
                frames[queue_index] = page
                queue_index = (queue_index + 1) % frame_count

        # Record step information
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


# -------------------------------------------------------------
# LRU Algorithm (Least Recently Used)
# Replaces the page that was not used for the longest time.
# -------------------------------------------------------------
def simulate_lru(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    steps = []
    last_used = {}  # Tracks when each page was last accessed

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
                # Find least recently used page
                lru_page = None
                lru_index = float("inf")

                for p in frames:
                    idx = last_used.get(p, -1)
                    if idx < lru_index:
                        lru_index = idx
                        lru_page = p

                replace_index = frames.index(lru_page)
                frames[replace_index] = page

        # Update last used time
        last_used[page] = current_index

        # Record step state
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


# -------------------------------------------------------------
# Optimal Algorithm
# Replaces the page that will not be used for the longest time in the future.
# -------------------------------------------------------------
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
                # Check future use of each page in memory
                farthest_index = -1
                page_to_replace = None

                for p in frames:
                    try:
                        next_use = pages.index(p, i + 1)
                    except ValueError:
                        next_use = float("inf")  # Not used again

                    if next_use > farthest_index:
                        farthest_index = next_use
                        page_to_replace = p

                replace_index = frames.index(page_to_replace)
                frames[replace_index] = page

        # Save step information
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


# -------------------------------------------------------------
# Helper: Print results in table format for console mode
# (GUI also uses these results but formats differently)
# -------------------------------------------------------------
def print_result(result):
    print(f"\nAlgorithm: {result['name']}")
    print("Step\tPage\tFrames\t\tResult")

    for idx, step in enumerate(result["steps"], start=1):
        frames_str = " ".join(str(x) for x in step["frames"])
        print(f"{idx}\t{step['page']}\t{frames_str:<10}\t{step['result']}")

    print(f"Total Page Faults: {result['page_faults']}")
    print(f"Total Hits: {result['hits']}")
    print(f"Hit Ratio: {result['hit_ratio']*100:.2f}%")


# -------------------------------------------------------------
# Main function for CLI usage (GUI users won't see this)
# -------------------------------------------------------------
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

    # Determine best algorithm
    all_results = [fifo_result, lru_result, optimal_result]
    best = min(all_results, key=lambda r: r["page_faults"])
    print(f"\nBest algorithm for this input (least page faults): {best['name']}")


if __name__ == "__main__":
    main()
