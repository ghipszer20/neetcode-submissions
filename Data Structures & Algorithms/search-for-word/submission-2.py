class Solution:
    def existAux(self, board, word, idx, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        
        if idx == len(word) - 1:
            return True
        
        board[i][j] = "Visited"

        return self.existAux(deepcopy(board), word, idx + 1, i + 1, j) or self.existAux(deepcopy(board), word, idx + 1, i, j + 1) or self.existAux(deepcopy(board), word, idx + 1, i - 1, j) or self.existAux(deepcopy(board), word, idx + 1, i, j - 1)
        
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.existAux(deepcopy(board), word, 0, i, j):
                        return True

        return False