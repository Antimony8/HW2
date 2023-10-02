import random

# Define a class to represent a 2D line segment
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Define the BSP tree node class
class BSPTreeNode:
    def __init__(self, line):
        self.line = line
        self.left = None
        self.right = None

# Function to construct a BSP tree recursively
def construct_bsp_tree(lines):
    if not lines:
        return None

    # Choose a partition line based on user input
    print("Available Lines:")
    for i, line in enumerate(lines):
        print(f"{i + 1}. Line: ({line.start}, {line.end})")

    while True:
        try:
            choice = int(input("Select a line (1 to N): "))
            if 1 <= choice <= len(lines):
                break
            else:
                print("Invalid choice. Please enter a valid line number.")
        except ValueError:
            print("Invalid input. Please enter a valid line number.")

    partition_line = lines[choice - 1]

    # Create a new BSP tree node for the partitioning line
    node = BSPTreeNode(partition_line)

    # Initialize lists for lines on the left and right sides of the partition
    left_lines = []
    right_lines = []

    for line in lines:
        if line != partition_line:
            # Determine which side of the partition the line falls on
            # (left, right, or both sides)
            # For simplicity, we assume lines that intersect the partition
            # line are split into left and right segments.

            # Check if the line starts on the left side and ends on the right side
            if (line.start < partition_line.start < line.end) or (line.start < partition_line.end < line.end):
                left_lines.append(line)
                right_lines.append(Line(partition_line.start, line.end))

            # Check if the line starts on the right side and ends on the left side
            elif (line.start > partition_line.start > line.end) or (line.start > partition_line.end > line.end):
                right_lines.append(line)
                left_lines.append(Line(partition_line.start, line.end))

            # Check if the line is completely on the left side
            elif line.start < partition_line.start and line.end < partition_line.start:
                left_lines.append(line)

            # Check if the line is completely on the right side
            elif line.start > partition_line.end and line.end > partition_line.end:
                right_lines.append(line)

    # Recursively construct the left and right subtrees
    node.left = construct_bsp_tree(left_lines)
    node.right = construct_bsp_tree(right_lines)

    return node

# Function for in-order traversal of the BSP tree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(f"Line: ({node.line.start}, {node.line.end})")
        inorder_traversal(node.right)

# Main program
if __name__ == "__main__":
    lines = [
        Line((-3, 2), (3, 2)),
        Line((-2, 2), (-2, -3)),
        Line((2, 2), (2, -3)),
        Line((-2, -2), (2, -2)),
        Line((0, 1), (0, 0)),
        Line((1, 0), (0, 0)),
        Line((1, 1), (0, 1))
    ]

    # Construct the BSP tree
    root = construct_bsp_tree(lines)

    # Perform an in-order traversal and print the lines
    print("In-Order Traversal of BSP Tree:")
    inorder_traversal(root)
