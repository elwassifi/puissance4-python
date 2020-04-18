import constante as cst
import copy
from move import Move

class Game():
    def get_best_col(self, grid, rows, ai_player, human_player):
        best_score = cst.NEG_INF
        best_col = int()
        for col in range(cst.NB_COL) :
            copy_grid = copy.deepcopy(grid)
            copy_rows = copy.deepcopy(rows)
            row = copy_rows[col]
            if row >= 0 :
                copy_grid[row+1][col+1] = ai_player.symbol
                copy_rows[col] -= 1
                score = self.min_max(ai_player, copy_grid, row+1, col+1, False, cst.DEPTH, cst.NEG_INF, cst.POS_INF, copy_rows, ai_player, human_player)
                if score > best_score :
                    best_score = score
                    best_col =  col+1
        return best_col

    def min_max(self, current_player, grid, row, col, is_maxi, depth, alpha, beta, available_rows, ai_player, human_player):
        move = self.evaluate_move(grid, row, col, current_player)

        if depth == 0 or self.is_gameover(move) :
            if current_player.is_ai :
                return move.score
            else :
                return - move.score

        if is_maxi :
            best_score = cst.NEG_INF
            for col in range(cst.NB_COL) :
                copy_grid = copy.deepcopy(grid)
                copy_available_rows = copy.deepcopy(available_rows)
                row = copy_available_rows[col]
                if row >= 0 :
                    copy_grid[row+1][col+1] = ai_player.symbol
                    copy_available_rows[col] -= 1
                    score =  self.min_max(ai_player,copy_grid, row+1, col+1, False, depth -1, alpha, beta, copy_available_rows, ai_player, human_player)
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha :
                        break
            return best_score
        else :
            best_score = cst.POS_INF
            for col in range(cst.NB_COL) :
                copy_grid = copy.deepcopy(grid)
                copy_available_rows = copy.deepcopy(available_rows)
                row = copy_available_rows[col]
                if row >= 0 :
                    copy_grid[row+1][col+1] = human_player.symbol
                    copy_available_rows[col] -= 1
                    score =  self.min_max(human_player,copy_grid, row+1, col+1, True, depth -1, alpha, beta, copy_available_rows, ai_player, human_player)
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha :
                        break
            return best_score

    def evaluate_move(self, grid, row, col, player):
        if self.count_aligned_symbol(grid, row, col) >= 4 :
            player.is_winner = True
            return Move(row, col, cst.CONNECT_4_SCROE, player)
        elif self.count_aligned_symbol(grid, row, col) == 3 :
            return Move(row, col, cst.CONNECT_3_SCROE, player)
        elif self.count_aligned_symbol(grid, row, col) == 2 :
            return Move(row, col, cst.CONNECT_2_SCROE, player)
        else:
            return Move(row, col, cst.CONNECT_1_SCROE, player)

    def is_gameover(self, move):
        if move.score == cst.CONNECT_4_SCROE:
            return True

    def is_draw(self, rows):
        for col in range(cst.NB_COL) :
            if rows[col] >= 0 :
                return False
        return True


    def count_aligned_symbol(self, grid, row, col):
        res = 1
        if grid[row][col] != -1 :
            res = max(res, self.count_aligned_symbol_by_xy(grid, row, col, 1, 1))
            res = max(res, self.count_aligned_symbol_by_xy(grid, row, col, 0, 1))
            res = max(res, self.count_aligned_symbol_by_xy(grid, row, col, -1,1))
            res = max(res, self.count_aligned_symbol_by_xy(grid, row, col, 1, 0))
        return res

    def count_aligned_symbol_by_xy(self, grid, row, col, y, x):
        symbol = grid[row][col]
        nb_aligned_symbol = 1

        row_of_y = row + y
        col_of_x = col + x

        while grid[row_of_y][col_of_x] == symbol :
            nb_aligned_symbol += 1
            row_of_y += y
            col_of_x  += x

        row_of_y = row - y
        col_of_x = col - x

        while grid[row_of_y][col_of_x] == symbol:
            nb_aligned_symbol += 1
            row_of_y -= y
            col_of_x  -= x

        return nb_aligned_symbol