class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edges = Counter()

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                edges[pos] += 1

        max_edges = max(edges.values(), default = 0)


        return len(wall) - max_edges