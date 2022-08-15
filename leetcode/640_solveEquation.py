class Solution(object):
    def solveEquation(self, equation):
        multi, number, i = 0, 0, 0
        left, add = 1, 1
        while i < len(equation):
            cur, add = 0, 1
            has_num = False
            if equation[i] == '=':
                left = -1
                i += 1
            if equation[i] == '+':
                add = 1
                i += 1
            if equation[i] == '-':
                add = -1
                i += 1
            while i < len(equation) and equation[i].isdigit():
                has_num = True
                cur = cur * 10 + int(equation[i])
                i += 1
            if i < len(equation) and equation[i] == 'x':
                multi += add * left * cur if has_num else left * add
                i += 1
            else:
                number += add * left * cur
        if multi == 0:
            return "Infinite solutions" if number == 0 else "No solution"
        return "x={}".format(-number / multi)

if __name__ == "__main__":
    solution = Solution()
    print(solution.solveEquation("3x=33+22+11"))