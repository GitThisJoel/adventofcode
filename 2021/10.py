import sys
import queue

left  = {'(', '{', '[', '<'}
right = {')', '}', ']', '>'}
pairs = {'()', '{}', '[]', '<>'}

def p1(input):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in input:
        line = line.strip()
        q = queue.LifoQueue()
        for c in line:
            if c in left:
                q.put(c)
            else:
                top = q.get()
                p = top+c
                if p not in pairs:
                    score += points[c]
    print("p1:", score)
    return

def p2(input):
        points = {'(': 1, '[': 2, '{': 3, '<': 4}
        scores = []
        for line in input:
            append = True
            score = 0
            line = line.strip()
            q = queue.LifoQueue()
            for c in line:
                if c in left:
                    q.put(c)
                else:
                    top = q.get()
                    p = top+c
                    if p not in pairs:
                        append = False
                        while not q.empty():
                            q.get()
                        break
            while not q.empty():
                score *= 5
                score += points[q.get()]
            if append:
                scores.append(score)
        scores.sort()
        print("p2:",scores[len(scores)//2])
        return

if __name__ == "__main__":
    input = [line for line in sys.stdin]
    p1(input)
    p2(input)
