| No. | Practical | Algorithm / Technique | Data Structure |
|---:|---|---|---|
| 1 | Vacuum Cleaner World | Simple Reflex Agent | Conditions |
| 2 | 8 Puzzle | A* Search | Priority Queue |
| 3 | Alpha-Beta Pruning | Adversarial Search | Game Tree |
| 4 | Tower of Hanoi | State Space Search | Recursion |
| 5 | Sudoku Solver | Backtracking + Constraint Propagation | Recursion |
| 6 | Traveling Salesman Problem | Local Beam Search | List |
| 7 | 8 Puzzle | BFS | Queue |
| 8 | Robot Path Planning | BFS | Queue |
| 9 | Blocks World | BFS | Queue |
| 10 | Water Jug Problem | DFS | Stack |
| 11 | Maze Solving | DFS | Stack |
| 12 | Blocks World | DFS | Stack |
| 13 | 8 Queens | Backtracking | Recursion |
| 14 | College Enquiry Chatbot | Rule-Based Pattern Matching | Conditions |
| 15 | Hospital Enquiry Chatbot | Rule-Based Pattern Matching | Conditions |
| 16 | Railway Enquiry Chatbot | Rule-Based Pattern Matching | Conditions |
| 17 | Online Shopping Chatbot | Rule-Based Pattern Matching | Conditions |
| 18 | Banking Enquiry Chatbot | Rule-Based Pattern Matching | Conditions |
| 19 | Blocks World | Goal Stack Planning | Stack |
| 20 | Game Playing Agent | Minimax | Game Tree |



------------------------------------------------------------------



Time & space complexity

| Algorithm / Practical | Time Complexity | Space Complexity |
|---|---|---|
| Simple Reflex Agent | O(1) | O(1) |
| A* Search | O(bᵈ) worst case | O(bᵈ) |
| Alpha-Beta Pruning | O(bᵈ) worst, O(bᵈ/²) best | O(bd) |
| Tower of Hanoi | O(2ⁿ) | O(n) |
| Sudoku Backtracking | O(9ᵐ) worst case | O(m) |
| Local Beam Search | O(k × n²) per iteration | O(k × n) |
| BFS – 8 Puzzle | O(V + E) | O(V) |
| BFS – Robot Planning | O(V + E) | O(V) |
| BFS – Blocks World | O(V + E) | O(V) |
| DFS – Water Jug | O(V + E) | O(V) |
| DFS – Maze | O(V + E) | O(V) |
| DFS – Blocks World | O(V + E) | O(V) |
| 8 Queens | O(N!) | O(N) |
| Rule-Based Chatbot | O(R) | O(R) |
| Goal Stack Planning | Exponential worst case | Exponential worst case |
| Minimax | O(bᵈ) | O(bd) |

Symbols:
-V = Number of vertices/states.
-E = Number of edges/transitions.
-b = Branching factor.
-d = Maximum search depth.
-n = Number of elements/blocks.
-N = Chessboard size.
-m = Number of empty Sudoku cells.
-k = Number of states maintained in Beam Search.
-R = Number of chatbot rules.
