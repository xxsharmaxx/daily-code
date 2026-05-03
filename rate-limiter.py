import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = []

    def allow_request(self):
        current_time = time.time()

        # Remove expired requests
        self.requests = [
            req for req in self.requests
            if current_time - req < self.time_window
        ]

        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True
        else:
            return False


# Create limiter: 5 requests per 10 seconds
limiter = RateLimiter(5, 10)

# Simulate requests
for i in range(10):
    if limiter.allow_request():
        print(f"Request {i+1}: ✅ Allowed")
    else:
        print(f"Request {i+1}: ❌ Blocked")

    time.sleep(1)
