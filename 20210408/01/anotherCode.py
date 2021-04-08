def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        print(p[i], p[stack[-1]])
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                print(ans, p[i], p[j], stack)
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    print(stack)
    print(ans)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    print(ans)
    return ans

solution([1, 2, 3, 2, 3, 1])