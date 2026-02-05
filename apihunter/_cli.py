import argparse
import sys
from dataclasses import dataclass
from typing import List

from ddgs import DDGS
from rich.pretty import pprint

from ._dorks import ApiHunterDorks
from ._settings import DDG_MAX_RESULT


@dataclass
class Args:
    target_domain: str | None
    target_organization: str | None
    max_results: int | None


class ApiHunterCli:
    def __init__(self, args: List[str]):

        self._args = args

    def run(self) -> None:
        parsed_args = self._parse_args()
        ddgs = DDGS()

        if not parsed_args.target_organization and parsed_args.target_domain:
            parsed_args.target_organization = parsed_args.target_domain.split(".")[-2]

        if not parsed_args.max_results:
            parsed_args.max_results = DDG_MAX_RESULT

        if not parsed_args.target_domain and not parsed_args.target_organization:
            sys.exit(1)

        dorks = ApiHunterDorks()

        pprint("[+] running first party dorks")

        for dork in dorks.first_party:
            query = dork.format(target_domain=parsed_args.target_domain)
            pprint("dork: " + query)
            results = ddgs.text(query, max_results=parsed_args.max_results)
            pprint(list(results))

        pprint("[+] running 3rd party dorks")

        for dork in dorks.third_party:
            query = dork.format(org=parsed_args.target_organization)
            results = ddgs.text(query, max_results=parsed_args.max_results)
            pprint("dork: " + query)
            pprint(list(results))

    def _parse_args(self) -> Args:
        parser = argparse.ArgumentParser(description="Hunt for API Collections")

        parser.add_argument("-d", "--target-domain", metavar="", type=str)
        parser.add_argument("-org", "--target-organization", metavar="", type=str)
        parser.add_argument("-results", "--max-results", metavar="", type=int)

        namespace = parser.parse_args(self._args)
        return Args(**vars(namespace))
