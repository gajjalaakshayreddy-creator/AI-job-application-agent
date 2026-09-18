import httpx

from src.collectors.greenhouse import GreenhouseCollector


def test_greenhouse_collector(monkeypatch):

    mock_response = {
        "jobs": [
            {
                "id": 123,
                "title": "AI Engineer",
                "updated_at": "2026-09-15T10:00:00Z",
                "location": {
                    "name": "Remote"
                },
                "absolute_url": (
                    "https://boards.greenhouse.io/"
                    "example/jobs/123"
                ),
                "content": (
                    "<p>Python and Azure experience required.</p>"
                ),
            }
        ]
    }

    def mock_get(*args, **kwargs):

        return httpx.Response(
            status_code=200,
            json=mock_response,
            request=httpx.Request(
                "GET",
                "https://example.com",
            ),
        )

    monkeypatch.setattr(httpx, "get", mock_get)

    collector = GreenhouseCollector("example")

    jobs = collector.fetch_jobs()

    assert len(jobs) == 1
    assert jobs[0].source == "greenhouse"
    assert jobs[0].external_job_id == "123"
    assert jobs[0].title == "AI Engineer"
    assert jobs[0].location == "Remote"
    assert "Python" in jobs[0].description