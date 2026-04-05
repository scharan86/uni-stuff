from collections import deque

def solve_water_jug():
    # Capacities: 4-gallon jug and 3-gallon jug
    # Goal: (2, 0)
    
    # Initial state
    start = (0, 0)
    goal = (2, 0)
    
    # Queue stores: (state, path_to_reach_this_state)
    queue = deque()
    queue.append((start, [start]))
    
    # Visited set to avoid revisiting states
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), path = queue.popleft()
        
        # Check if goal reached
        if (x, y) == goal:
            print("Solution found!")
            print(f"Total steps: {len(path) - 1}")
            print("\nSequence of states:")
            for i, state in enumerate(path):
                print(f"Step {i}: ({state[0]}, {state[1]})")
            return path
        
        # Generate all possible next states
        next_states = []
        
        # 1. Fill 4-gallon jug
        next_states.append((4, y))
        
        # 2. Fill 3-gallon jug
        next_states.append((x, 3))
        
        # 3. Empty 4-gallon jug
        next_states.append((0, y))
        
        # 4. Empty 3-gallon jug
        next_states.append((x, 0))
        
        # 5. Pour from 4-gallon to 3-gallon
        pour = min(x, 3 - y)
        next_states.append((x - pour, y + pour))
        
        # 6. Pour from 3-gallon to 4-gallon
        pour = min(y, 4 - x)
        next_states.append((x + pour, y - pour))
        
        # Explore each next state
        for new_state in next_states:
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))
    
    print("No solution found!")
    return None

# Run the solver
if __name__ == "__main__":
    solve_water_jug()
