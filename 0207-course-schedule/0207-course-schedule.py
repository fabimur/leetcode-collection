from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for course, req in prerequisites:
            graph[course].append(req)


        path = set()
        checked = set()
        for node in list(graph):
            if self.checkCycles(graph, node, path, checked):
                return False

        return True

    def checkCycles(self, graph, node, path, checked) -> bool:
        if node in checked:
            return False

        if node in path:
            return True
        
        path.add(node)
        for n in graph[node]:
            if self.checkCycles(graph, n, path, checked):
                return True

        path.remove(node)
        checked.add(node)
        return False