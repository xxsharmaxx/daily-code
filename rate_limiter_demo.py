import time
from collections import defaultdict, deque


class RateLimiter:

    def __init__(self, max_requests=5, window=10):
        self.max_requests = max_requests
        self.window = window
        self.requests = defaultdict(deque)

    def allow_request(self, client):
        now = time.time()

        history = self.requests[client]

        # Remove expired requests
        while history and now - history[0] >= self.window:
            history.popleft()

        # Check rate limit
        if len(history) >= self.max_requests:
            return False, len(history)

        history.append(now)

        return True, len(history)

    def remaining(self, client):
        now = time.time()
        history = self.requests[client]

        while history and now - history[0] >= self.window:
            history.popleft()

        return max(
            0,
            self.max_requests - len(history)
        )


def main():

    limiter = RateLimiter(
        max_requests=5,
        window=10
    )

    print("=" * 60)
    print("              API RATE LIMITER")
    print("=" * 60)

    print("\nLimit: 5 requests / 10 seconds")
    print("Type 'exit' to stop.\n")

    while True:

        client = input(
            "Client ID: "
        ).strip()

        if client.lower() == "exit":
            break

        allowed, used = limiter.allow_request(client)

        remaining = limiter.remaining(client)

        if allowed:

            print(
                f"  ✅ ALLOWED | "
                f"Used: {used}/5 | "
                f"Remaining: {remaining}"
            )

        else:

            print(
                f"  🚫 BLOCKED | "
                f"Rate limit exceeded | "
                f"Retry after {limiter.window}s"
            )

        print("-" * 60)


if __name__ == "__main__":
    main()
