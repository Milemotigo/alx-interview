#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    is_visited = [False] * len(boxes)
    is_visited[0] = True
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            # If the key can open an unvisited box
            if not is_visited[key]:
                is_visited[key] = True
                stack.append(key)
    return all(is_visited)