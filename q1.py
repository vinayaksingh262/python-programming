def isBalanced(expr):

    flag = True
    count = 0

    for char in expr:
        if char == "{":
            count += 1
        else:

            count -= 1
        if count < 0:

            flag = False
            break

    if count != 0:
        flag = False

    return flag


def recur(expr, n, ind, change, ans):

    if ind == n:
        if isBalanced(expr):
            ans[0] = min(ans[0], change)
        return

    recur(expr, n, ind + 1, change, ans)

    if expr[ind] == "{":
        expr = expr[:ind] + "}" + expr[ind + 1 :]
    else:
        expr = expr[:ind] + "{" + expr[ind + 1 :]
    recur(expr, n, ind + 1, change + 1, ans)


def countMinReversals(expr):

    n = len(expr)

    ans = [float("inf")]

    if n % 2 == 1:
        return -1
    else:

        recur(expr, n, 0, 0, ans)
        if ans[0] == float("inf"):
            return -1
        return ans[0]


if __name__ == "__main__":
    expr = input("Enter the brackets: ")
    result = countMinReversals(expr)
    print(result)
