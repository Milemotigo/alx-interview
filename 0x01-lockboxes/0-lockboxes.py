def canUnlockAll(boxes):
    # Create a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Start with the first box which is unlocked
    stack = [0]  # Initialize a stack with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)

    # If all boxes are visited, return True; otherwise, return False
    return all(visited)

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))