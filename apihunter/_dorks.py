class ApiHunterDorks:
    """Search query templates for discovering API documentation."""

    def __init__(self):
        """Initialize predefined dork templates.

        Attributes:
            api_docs: Search queries for discovering first-party API
                documentation hosted on a target domain.
            third_party: Search queries for discovering third-party API
                documentation (e.g., Postman collections).
        """
        self.first_party = [
            "site:{target_domain} inurl:/api",
            'site:{target_domain} "API documentation"',
            'site:{target_domain} "Developer documentation"',
            'site:{target_domain} "Developer docs"',
        ]

        self.third_party = [
            "site:postman.com intext:{org}",
            "site:swaggerhub.com/apis {org}",
            "site:apis.guru {org}",
            "site:rapidapi.com {org}",
            "site:stoplight.io {org}",
            "site:gitbook.io {org}",
        ]

    @staticmethod
    def format(dork: str, **values: str) -> str:
        """Format a single dork template with the given values."""
        return dork.format(**values)
