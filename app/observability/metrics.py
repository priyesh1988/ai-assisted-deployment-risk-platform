
from prometheus_client import Counter

risk_requests = Counter("risk_requests_total", "Total risk scoring requests")
