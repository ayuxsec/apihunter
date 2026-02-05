import argparse
import logging
import sys
from dataclasses import dataclass
from typing import Iterable, List, Optional

from ddgs import DDGS
from rich.pretty import pprint

from ._dorks import ApiHunterDorks
from ._settings import DDG_MAX_RESULT

logger = logging.getLogger(__name__)


@dataclass
class Args:
    target_domain: Optional[str]
    target_organization: Optional[str]
    max_results: int


class ApiHunterCli:
    def __init__(self, argv: List[str]) -> None:
        self._argv = argv
        self._ddgs = DDGS()
        self._dorks = ApiHunterDorks()

    def run(self) -> None:
        args = self._parse_args()
        self._normalize_args(args)

        if not (args.target_domain or args.target_organization):
            logger.error("Either target domain or target organization must be provided")
            sys.exit(1)

        self._run_dorks(
            label="[+] running first party dorks",
            dorks=self._dorks.first_party,
            formatter=lambda d: d.format(target_domain=args.target_domain),
            max_results=args.max_results,
        )

        self._run_dorks(
            label="[+] running 3rd party dorks",
            dorks=self._dorks.third_party,
            formatter=lambda d: d.format(org=args.target_organization),
            max_results=args.max_results,
        )

    @staticmethod
    def _normalize_args(args: Args) -> None:
        if not args.max_results:
            args.max_results = DDG_MAX_RESULT

        if not args.target_organization and args.target_domain:
            parts = args.target_domain.split(".")
            if len(parts) >= 2:
                args.target_organization = parts[-2]

    def _run_dorks(
        self,
        *,
        label: str,
        dorks: Iterable[str],
        formatter,
        max_results: int,
    ) -> None:
        pprint(label)

        for dork in dorks:
            query = formatter(dork)
            pprint(f"dork: {query}")

            try:
                results = self._ddgs.text(query, max_results=max_results)
                pprint(list(results))
            except Exception as exc:
                logger.error("Search failed for query '%s': %s", query, exc)

    def _parse_args(self) -> Args:
        parser = argparse.ArgumentParser(description="Hunt for API collections")

        parser.add_argument("-d", "--target-domain", type=str)
        parser.add_argument("-org", "--target-organization", type=str)
        parser.add_argument("-r", "--max-results", type=int)

        namespace = parser.parse_args(self._argv)

        return Args(
            target_domain=namespace.target_domain,
            target_organization=namespace.target_organization,
            max_results=namespace.max_results,
        )
