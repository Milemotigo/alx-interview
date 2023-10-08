#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked using keys found in the boxes.

    Args:
        boxes (list of lists): A list of boxes, where each box is represented as a list of keys.

    Returns:
        bool: true if all boxes can be unlocked, False otherwise.
    """

    is_visited = [False] * len(boxes)

    is_visited[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        if key in boxes[current_box]:
            # If the key can open an unvisited box
            if not is_visited[key]:
                is_visited[key] = True

                stack.append(key)
        
        return all(is_visited)