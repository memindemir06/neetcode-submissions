class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 1 : ((0,3,6),(0,3),((0,0)))

        # 1 : [(0,0), ]

        # 1 -> same x, diff y
        # 2 -> same y, diff x
        # 3 -> same grid box -> x1-x2 < 3 and y1-y2 < 3

        seen = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                digit = board[i][j]
                if digit == ".":
                    continue
                if digit not in seen:
                    seen[digit] = [(i,j)]
                    continue
                for pair in seen[digit]:
                    x, y = pair
                    if (x // 3 == i // 3 and y // 3 == j // 3) or x == i or y == j:
                        return False
                seen[digit].append((i,j))

        return True

