class ListNode:
    def __init__(self, url: str):
        self.val = url
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        if 1 <= len(homepage) <= 20:
            start = ListNode(homepage)
            self.current = start
        else:
            raise ValueError("homepage url not in range")

    def visit(self, url: str) -> None:
        if 1 <= len(url) <= 20:
            new = ListNode(url)
            new.prev = self.current
            self.current.next = new
            self.current = new
            return
        else:
            raise ValueError("url not in range")

    def back(self, steps: int) -> str:
        if 1 <= steps <= 100 and self.current:
            while steps > 0 and self.current.prev:
                self.current = self.current.prev
                steps -= 1
        else:
            raise ValueError("steps not in range")
        return self.current.val



    def forward(self, steps: int) -> str:
        if 1 <= steps <= 100 and self.current:
            while steps > 0 and self.current.next:
                self.current = self.current.next
                steps -= 1
        else:
            raise ValueError("steps not in range")
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)