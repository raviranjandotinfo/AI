import heapq

class Node:
	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position

	def __repr__(self):
		return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

	def __lt__(self, other):
		return self.f < other.f

	def __gt__(self, other):
		return self.f > other.f

def calc_manhattan(curr, goal):
	return abs(curr[0] - goal[0]) + abs(curr[1] - goal[1])

def calc_euclidean(curr, goal):
	return ((curr[0] - goal[0]) ** 2) + ((curr[1] - goal[1]) ** 2) 


def get_path(current_node):
	path = []
	current = current_node
	while current is not None:
		path.append(current.position)
		current = current.parent
	return path[::-1]

def print_maze(maze, start, end, path = None):
	if path:
		for p in path:
			maze[p[0]][p[1]] = "*"
	maze[start[0]][start[1]] = "A"
	maze[end[0]][end[1]] = "B"
	for row in maze:
		print("".join(row))


def Astar(maze, start, end, allow_diagonal= False):
	start_node = Node(position = start)
	end_node = Node(position = end)

	open_list = []
	closed_list  = []

	heapq.heapify(open_list)
	heapq.heappush(open_list, start_node)

	adjacent_pos = ((0,-1), (0,1), (-1,0), (1,0))
	if allow_diagonal:
		adjacent_pos = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)
	
	while len(open_list) > 0:
		current_node = heapq.heappop(open_list)
		closed_list.append(current_node)

		if current_node == end_node:
			return get_path(current_node)

		children = []
		for new_pos in adjacent_pos:
			node_position = (current_node.position[0] + new_pos[0], 
							current_node.position[1] + new_pos[1])

			# Non reachable
			if maze[node_position[0]][node_position[1]] == "#":
				continue

			new_node = Node(current_node, node_position)
			children.append(new_node)
		for child in children:
			if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
				continue

			child.g = current_node.g + 1
			if not allow_diagonal:
				child.h = calc_manhattan(child.position, end_node.position)
			if allow_diagonal:
				child.h = calc_euclidean(child.position, end_node.position)
			child.f = child.g + child.h

			if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
				continue

			heapq.heappush(open_list, child)

	return None

maze = [ [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ],
        [ '#', 'A', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#' ],
        [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', '#' ],
        [ '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#' ]]
start_x = 1
start_y = 1
end_x = 18
end_y = 18


def main():
    start = (start_x, start_y)
    end = (end_x, end_y)
    path = Astar(maze, start, end)
    path= None
    print_maze(maze, start, end, path)
    path = Astar(maze, start, end, allow_diagonal=False)
    print_maze(maze, start, end, path)

main()
