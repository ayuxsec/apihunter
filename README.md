## Install

```bash
pip install git+https://github.com/ayuxsec/apihunter.git
```

## Usage

Example output:

```console
$ apihunter -d hackerone.com -org hackerone
'[+] running first party dorks'
'dork: site:hackerone.com inurl:/api'
INFO | primp | response: https://en.wikipedia.org/w/api.php?action=opensearch&profile=fuzzy&limit=1&search=site%3Ahackerone.com%20inurl%3A/api 200
INFO | httpx | HTTP Request: POST https://html.duckduckgo.com/html/ "HTTP/2 200 OK"
INFO | primp | response: https://grokipedia.com/api/typeahead?query=site%3Ahackerone.com+inurl%3A%2Fapi&limit=1 200
INFO | primp | response: https://www.google.com/search?q=site%3Ahackerone.com+inurl%3A%2Fapi&filter=1&start=0&hl=en-US&lr=lang_en&cr=countryUS 200
INFO | primp | response: https://yandex.com/search/site/?text=site%3Ahackerone.com+inurl%3A%2Fapi&web=1&searchid=8087528 200
INFO | primp | response: https://www.mojeek.com/search?q=site%3Ahackerone.com+inurl%3A%2Fapi 403
INFO | primp | response: https://search.brave.com/search?q=site%3Ahackerone.com+inurl%3A%2Fapi&source=web 429
[
│   {
│   │   'title': 'Pentesting for APIs and Best Practices - HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/penetration-testing-api',
│   │   'body': "HackerOne's community-driven Pentest as a Service (PTaaS) uncovers vulnerabilities specific to APIs , leveraging expert methodologies and tailored testing approaches."
│   },
│   {
│   │   'title': 'HackerOne API',
│   │   'href': 'https://api.hackerone.com/',
│   │   'body': "HackerOne API Documentation What can you do with our API ? Pull vulnerability reports Pull all of your program's vulnerability reports into your own systems to automate your workflows. Learn about Reports"
│   },
│   {
│   │   'title': 'Getting Started - HackerOne API',
│   │   'href': 'https://api.hackerone.com/getting-started-hacker-api/',
│   │   'body': "API tokens can be generated from your Settings if you're already using the HackerOne Professional, Community, or Enterprise edition. If you're unable to generate an API token, please contact support To get started with the HackerOne API : Generate an API Token. Go to Hacker Resources and choose the endpoint you want to pull information from."
│   },
│   {
│   │   'title': 'Use Cases - HackerOne API',
│   │   'href': 'https://api.hackerone.com/use-cases/',
│   │   'body': 'Use Cases The API is made for customers that have a need to access and interact with their HackerOne report and program data and be able to automate their workflows. Customers use this to generate dashboards, automatically escalate reports to their internal systems, assign users based on the on-call personnel or when an internal ticket is resolved, interact with the reporters, and more. The ...'
│   },
│   {
│   │   'title': 'Reference - API Documentation',
│   │   'href': 'https://api.hackerone.com/hacker-reference/',
│   │   'body': 'Hacker Reference The following section contains a complete reference of all the objects that can be returned through the API . Objects that have been explained earlier in this documentation are not included. The objects in this section are never top level resources by themselves and will only be returned as sub resources. All objects are made up of an id and a type attribute. With those ...'
│   },
│   {
│   │   'title': 'API Documentation - HackerOne',
│   │   'href': 'https://api.hackerone.com/customer-reference/',
│   │   'body': 'The following section contains a complete reference of all the objects that can be returned through the API . Objects that have been explained earlier in this documentation are not included. The objects in this section are never top level resources by themselves and will only be returned as sub resources.'
│   },
│   {
│   │   'title': 'Getting Started - HackerOne API',
│   │   'href': 'https://api.hackerone.com/getting-started/',
│   │   'body': "API tokens can be generated from your Program Settings if you're already using the HackerOne Professional, Community, or Enterprise edition. If you can't generate an API token, you can contact sales to upgrade your program or create a test program to experiment with the API . To get started with the HackerOne API : Generate an API Token."
│   },
│   {
│   │   'title': 'HackerOne API v1',
│   │   'href': 'https://api.hackerone.com/customer-resources/',
│   │   'body': "importrequestsheaders={'Accept':'application/json'}r=requests.get('https:// api .hackerone.com/v1/activities/ {id}',auth=('','<YOUR_API_TOKEN ..."
│   },
│   {
│   │   'title': 'Webhooks - HackerOne API',
│   │   'href': 'https://api.hackerone.com/webhooks/',
│   │   'body': "Webhooks Webhooks enable you to build your own real-time integrations that subscribe to certain report and program events on HackerOne. They can be used to: Update an external issue tracker Trigger a notification system Update a report's data backup Trigger provisioning for a user account When one of those events is triggered, we'll send an HTTP POST payload to the webhook's configured URL ..."
│   },
│   {
│   │   'title': 'HackerOne',
│   │   'href': 'https://hackerone.com/reports/1218680',
│   │   'body': 'At Dev Role with Limited Engine Access, an user still can access API endpoint `/ api /as/v1/credentials/` to get all API keys (private-key, search-key ... ) ## Steps To Reproduce: 1 - Log in Kibana with the admin (elastic) user and go to the Stack Management > Users page...'
│   },
│   {
│   │   'title': "How the Industry's First Hacker-Powered API Helps ...",
│   │   'href': 'https://www.hackerone.com/blog/how-industrys-first-hacker-powered-api-helps-hackers-automate-workflows',
│   │   'body': "15 Jul 2021 · HackerOne's new set of API endpoints saves time. It increases hacker job satisfaction by automating regular tasks, freeing them up to bug hunt."
│   },
│   {
│   │   'title': 'Announcing the HackerOne API',
│   │   'href': 'https://www.hackerone.com/blog/announcing-hackerone-api',
│   │   'body': '1 Jun 2016 · The HackerOne API allows for custom metrics, beyond those found in HackerOne, and offers organizations access to raw report data and a powerful ...'
│   },
│   {
│   │   'title': "Introducing HackerOne's Hai API: Revolutionize Your Workflow ...",
│   │   'href': 'https://www.hackerone.com/blog/introducing-hackerones-hai-api-revolutionize-your-workflow-automation-ai',
│   │   'body': "28 Jun 2024 · Hai is HackerOne's embedded AI assistant designed to make your journey through vulnerability reports and hacker interactions smoother and more insightful."
│   },
│   {
│   │   'title': 'API Update Announcement: Report State Changes and Submission ...',
│   │   'href': 'https://www.hackerone.com/blog/api-update-announcement-report-state-changes-and-submission-comments',
│   │   'body': "10 Nov 2016 · Today, we're announcing an update to the HackerOne API with some slick new communication features. Now, all Pro and Enterprise subscribers have ..."
│   },
│   {
│   │   'title': 'Start Hacking & Join the Largest Hacker Community | HackerOne',
│   │   'href': 'https://www.hackerone.com/hackers/how-to-start-hacking',
│   │   'body': 'Get rewarded for hacking. Companies and organizations on our platform want to hear from you about security vulnerabilities they might have overlooked across their websites, APIs ...'
│   },
│   {
│   │   'title': 'HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/category/application-security',
│   │   'body': 'Hack, learn, earn. See what the HackerOne community is all about.'
│   },
│   {
│   │   'title': 'AI Red Teaming | Offensive Testing for AI Models | HackerOne',
│   │   'href': 'https://www.hackerone.com/product/ai-red-teaming',
│   │   'body': 'HackerOne AI Red Teaming applies adversarial testing to your models, APIs , and integrations to reveal high-impact safety, security, and trust issues.'
│   },
│   {
│   │   'title': 'Hai Triage | HackerOne',
│   │   'href': 'https://www.hackerone.com/platform/triage',
│   │   'body': 'Standard Managed Triage. Web, Mobile, and API . Bounty Advisement. Escalation to in-house ticketing system (Jira, ServiceNow, etc.) Hacker Engagement and Mediation.'
│   },
│   {
│   │   'title': 'Pentesting for AI and Large Language Models | HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/pentesting-ai-and-large-language-models',
│   │   'body': "Today, technological advancements in Large Language Models (LLMs) and the artificial intelligence (AI) behind them have reignited discussions around Turing's original concept."
│   }
]
'dork: site:hackerone.com "API documentation"'
INFO | primp | response: https://en.wikipedia.org/w/api.php?action=opensearch&profile=fuzzy&limit=1&search=site%3Ahackerone.com%20%22API%20documentation%22 200
INFO | primp | response: https://www.google.com/search?q=site%3Ahackerone.com+%22API+documentation%22&filter=1&start=0&hl=en-US&lr=lang_en&cr=countryUS 200
INFO | primp | response: https://grokipedia.com/api/typeahead?query=site%3Ahackerone.com+%22API+documentation%22&limit=1 200
INFO | httpx | HTTP Request: POST https://html.duckduckgo.com/html/ "HTTP/2 200 OK"
INFO | primp | response: https://yandex.com/search/site/?text=site%3Ahackerone.com+%22API+documentation%22&web=1&searchid=3324592 200
INFO | primp | response: https://www.mojeek.com/search?q=site%3Ahackerone.com+%22API+documentation%22 403
INFO | primp | response: https://search.brave.com/search?q=site%3Ahackerone.com+%22API+documentation%22&source=web 200
[
│   {
│   │   'title': 'API Documentation - HackerOne',
│   │   'href': 'https://api.hackerone.com/customer-reference/',
│   │   'body': 'The following section contains a complete reference of all the objects that can be returned through the API. Objects that have been explained earlier in this documentation are not included. The objects in this section are never top level resources by themselves and will only be returned as sub resources.'
│   },
│   {
│   │   'title': 'HackerOne API Documentation',
│   │   'href': 'https://api.hackerone.com/',
│   │   'body': "HackerOne API Documentation What can you do with our API? Pull vulnerability reports Pull all of your program's vulnerability reports into your own systems to automate your workflows. Learn about Reports"
│   },
│   {
│   │   'title': 'Reference - API Documentation',
│   │   'href': 'https://api.hackerone.com/hacker-reference/',
│   │   'body': 'Hacker Reference The following section contains a complete reference of all the objects that can be returned through the API. Objects that have been explained earlier in this documentation are not included. The objects in this section are never top level resources by themselves and will only be returned as sub resources. All objects are made up of an id and a type attribute. With those ...'
│   },
│   {
│   │   'title': 'Announcing the HackerOne API | HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/announcing-hackerone-api',
│   │   'body': 'The API documentation can be found at https://api.hackerone.com/docs/v1. The code examples in the documentation all work, so we encourage you to play around with it and see if the API is right for you.'
│   },
│   {
│   │   'title': 'Why You Need To Focus on Improving Your API Docs | HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/why-you-need-focus-improving-your-api-docs',
│   │   'body': 'Not long, developers give up on an API with mediocre documentation almost immediately. You have to grab their attention and walk them through the first steps in just a few short minutes.'
│   },
│   {
│   │   'title': 'Generating TypeScript Types with OpenAPI for REST API Consumption | HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/generating-typescript-types-openapi-rest-api-consumption',
│   │   'body': 'OpenAPI Generator: The OpenAPI Generator project offers extensive documentation on how to generate client libraries, server stubs, API documentation , and other useful components from an OpenAPI Specification.'
│   },
│   {
│   │   'title': 'Report #745171 - Unprotected and Test site API Exposes ...',
│   │   'href': 'https://hackerone.com/reports/745171',
│   │   'body': 'Description: While performing manual reconnaissance, I came across Swagger/API documentation for the ··· web services API at https://·······/. The ...'
│   },
│   {
│   │   'title': 'Audit Logs | HackerOne Help Center',
│   │   'href': 'https://docs.hackerone.com/en/articles/8524901-audit-logs',
│   │   'body': 'See this article from the HackerOne API documentation to learn more: https://api.hackerone.com/customer-resources/#programs-get-audit-log. Note: You must be ...'
│   },
│   {
│   │   'title': 'LaunchDarkly - Bug Bounty Program - HackerOne',
│   │   'href': 'https://hackerone.com/launchdarkly/policy_versions',
│   │   'body': '... API documentation may be found here: [API docs](https://apidocs.launchdarkly.com/) The `/api/v2/` and `/internal/` subroutes are customer-facing APIs and ...'
│   },
│   {
│   │   'title': 'Rocket.Chat | Report #219957 - XSS via /api/v1/chat.postMessage',
│   │   'href': 'https://hackerone.com/reports/219957',
│   │   'body': 'Description: According to the API documentation chat messages can have attachments. These attachments then can have fields which contain a title and ...'
│   },
│   {
│   │   'title': 'Acessed internal api documentation and information',
│   │   'href': 'https://hackerone.com/reports/1049733',
│   │   'body': 'Sign in to HackerOne.'
│   },
│   {
│   │   'title': 'Webhooks | HackerOne Help Center',
│   │   'href': 'https://docs.hackerone.com/organizations/webhooks.html',
│   │   'body': 'Webhooks enable you to build your own real-time integrations that subscribe to certain report and program events on HackerOne. When an event is triggered, HackerOne will send an HTTP POST payload to the webhook’s configured URL. View the API documentation for webhooks.'
│   },
│   {
│   │   'title': 'Export Reports | HackerOne Help Center',
│   │   'href': 'https://docs.hackerone.com/en/articles/8514502-export-reports',
│   │   'body': 'You can also export reports by utilizing the API. See these articles from the HackerOne API documentation to learn more:'
│   },
│   {
│   │   'title': 'Audit Logs | HackerOne Help Center',
│   │   'href': 'https://docs.hackerone.com/organizations/audit-logs.html',
│   │   'body': 'You can also access the audit log via the API. See this article from the HackerOne API documentation to learn more: https://api.hackerone.com/customer-resources/#programs-get-audit-log'
│   },
│   {
│   │   'title': 'New Relic disclosed on HackerOne: Getting API access key Through ...',
│   │   'href': 'https://hackerone.com/reports/969456',
│   │   'body': 'If we can fetch the entire back-end API documentation and calls available on a server then that can be very dangerous is many cases what if we could get our hands on some API calls only meant to be used internally To test a server for GraphQL introspection misconfiguration: 1) Intercept...'
│   },
│   {
│   │   'title': 'Liberapay disclosed on HackerOne: Anyone can register organization...',
│   │   'href': 'https://hackerone.com/reports/361189',
│   │   'body': 'When another value is provided, an error message is printed saying the Legal Type is wrong. This error message is not printed and request success when the value "Soletrader" is provided. The value "Soletrader" is part of the MangoPay API Documentation ( ). A...'
│   }
]
'dork: site:hackerone.com "Developer documentation"'
INFO | primp | response: https://en.wikipedia.org/w/api.php?action=opensearch&profile=fuzzy&limit=1&search=site%3Ahackerone.com%20%22Developer%20documentation%22 200
INFO | primp | response: https://www.mojeek.com/search?q=site%3Ahackerone.com+%22Developer+documentation%22 403
INFO | primp | response: https://grokipedia.com/api/typeahead?query=site%3Ahackerone.com+%22Developer+documentation%22&limit=1 200
INFO | primp | response: https://search.brave.com/search?q=site%3Ahackerone.com+%22Developer+documentation%22&source=web 429
INFO | httpx | HTTP Request: POST https://html.duckduckgo.com/html/ "HTTP/2 202 Accepted"
INFO | primp | response: https://www.google.com/search?q=site%3Ahackerone.com+%22Developer+documentation%22&filter=1&start=0&hl=en-US&lr=lang_en&cr=countryUS 200
INFO | primp | response: https://search.yahoo.com/search;_ylt=sQh_jcv5PIrm5YT6pfkFyZgQ;_ylu=QzPVheD9xAty77X0xPAuzsQ8f2vFTDnXmP6oTVF_SKalisk?p=site%3Ahackerone.com+%22Developer+documentation%22 200
INFO | primp | response: https://yandex.com/search/site/?text=site%3Ahackerone.com+%22Developer+documentation%22&web=1&searchid=4519626 200
[
│   {
│   │   'title': 'Why You Need To Focus on Improving Your API Docs | HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/why-you-need-focus-improving-your-api-docs',
│   │   'body': 'A key first step is to build out robust developer documentation . Sites packed with helpful content like quick start guides, code examples, tutorials, and coding playgrounds.'
│   },
│   {
│   │   'title': 'HackerOne',
│   │   'href': 'https://hackerone.com/reports/2174818',
│   │   'body': 'Cloudflare relies on Swagger to present API Docs within our Developer Documentation . Swagger incorporates a feature known as "schema_url," which permits the rendering of a YAML schema from a remote URL.'
│   },
│   {
│   │   'title': 'Yoti - Bug Bounty Program | HackerOne',
│   │   'href': 'https://hackerone.com/yoti/policy_versions',
│   │   'body': "- **Developer Documentation Site**: Testing on [DEVELOPERS.YOTI.COM](https://developers.yoti.com) is strictly prohibited, as it's a third-party hosted site ..."
│   },
│   {
│   │   'title': 'Glassdoor | Bug Bounty Program Policy - HackerOne',
│   │   'href': 'https://hackerone.com/glassdoor',
│   │   'body': "Developer Documentation Focus areas: privilege escalation, sensitive data exposure. https://www.glassdoor.com/*, Glassdoor's primary web application. A good ..."
│   },
│   {
│   │   'title': 'Uber disclosed on HackerOne: HTML Escaping Error in the 404 Page on...',
│   │   'href': 'https://hackerone.com/reports/125130',
│   │   'body': "We actually forward developer.uber.com/docs/ through to readme.io for our developer documentation, I'll see that this gets forwarded over to them for ..."
│   },
│   {
│   │   'title': 'Glassdoor - Bug Bounty Program | HackerOne',
│   │   'href': 'https://hackerone.com/glassdoor/policy_versions',
│   │   'body': '[Developer Documentation](https://www.glassdoor.com/developer/index.htm) *Focus areas: privilege escalation, sensitive data exposure* | | | https://www ...'
│   },
│   {
│   │   'title': 'Mapbox - HackerOne',
│   │   'href': 'https://hackerone.com/mapbox/policy_scopes',
│   │   'body': 'Mapbox developer documentation that provides comprehensive guides and references services. Accounts Service APIs · Maps Service APIs · Navigation Service APIs ...'
│   },
│   {
│   │   'title': 'Yoti | Bug Bounty Program Policy - HackerOne',
│   │   'href': 'https://hackerone.com/yoti',
│   │   'body': "Developer Documentation Site: Testing on DEVELOPERS.YOTI.COM is strictly prohibited, as it's a third-party hosted site and not part of our security concerns."
│   },
│   {
│   │   'title': 'Bug Bounty Program | HackerOne',
│   │   'href': 'https://hackerone.com/cloudflare/policy_versions?type=team',
│   │   'body': '19 Jun 2024 · For research into our products, good starting points include our [Developer documentation](https://developers.cloudflare.com/docs/), [API ...'
│   },
│   {
│   │   'title': 'Navigating the Perils of Race Conditions in iOS App... | HackerOne',
│   │   'href': 'https://www.hackerone.com/blog/navigating-perils-race-conditions-ios-app-development',
│   │   'body': 'For further reading on iOS concurrency and best practices, the Apple Developer Documentation provides comprehensive guides and references.'
│   },
│   {
│   │   'title': 'Report #2923061 - API Key Exposed in JavaScript File on 1Password ...',
│   │   'href': 'https://hackerone.com/reports/2923061',
│   │   'body': '18 Jul 2025 · The researcher reported an API key exposed within a JavaScript file on our public developer documentation site ( developer.1password.com ).'
│   }
]
'dork: site:hackerone.com "Developer docs"'
INFO | primp | response: https://en.wikipedia.org/w/api.php?action=opensearch&profile=fuzzy&limit=1&search=site%3Ahackerone.com%20%22Developer%20docs%22 200
INFO | primp | response: https://search.yahoo.com/search;_ylt=RJiNaoO7jRgzESx5a_8t83VL;_ylu=Y40tTbk8voUsdd2xBB8q7mms2irK8N0Ah8tj5dNXEhuCc4o?p=site%3Ahackerone.com+%22Developer+docs%22 200
INFO | primp | response: https://grokipedia.com/api/typeahead?query=site%3Ahackerone.com+%22Developer+docs%22&limit=1 200
INFO | httpx | HTTP Request: POST https://html.duckduckgo.com/html/ "HTTP/2 202 Accepted"
INFO | primp | response: https://search.brave.com/search?q=site%3Ahackerone.com+%22Developer+docs%22&source=web 429
INFO | primp | response: https://yandex.com/search/site/?text=site%3Ahackerone.com+%22Developer+docs%22&web=1&searchid=9618897 200
INFO | primp | response: https://www.google.com/search?q=site%3Ahackerone.com+%22Developer+docs%22&filter=1&start=0&hl=en-US&lr=lang_en&cr=countryUS 200
INFO | primp | response: https://www.mojeek.com/search?q=site%3Ahackerone.com+%22Developer+docs%22 403
[
│   {
│   │   'title': 'Magic | Updates - HackerOne',
│   │   'href': 'https://hackerone.com/magic-bbp/updates',
│   │   'body': 'Features/links that lead to or are provided by external providers i.e our Typeform integrations, developer docs, etc. Our API endpoint (api.fortmatic.com) ...'
│   },
│   {
│   │   'title': 'X / xAI | Report #885539 - Private list members disclosure via GraphQL',
│   │   'href': 'https://hackerone.com/reports/885539',
│   │   'body': "Fortunately, Twitter's API rate limits were mostly broken. Even though Twitter's developer docs said that there was a rate limit, there were many that didn't."
│   }
]
'[+] running 3rd party dorks'
'dork: site:postman.com hackerone'
INFO | httpx | HTTP Request: POST https://html.duckduckgo.com/html/ "HTTP/2 202 Accepted"
INFO | primp | response: https://en.wikipedia.org/w/api.php?action=opensearch&profile=fuzzy&limit=1&search=site%3Apostman.com%20hackerone 200
INFO | primp | response: https://grokipedia.com/api/typeahead?query=site%3Apostman.com+hackerone&limit=1 200
INFO | primp | response: https://www.google.com/search?q=site%3Apostman.com+hackerone&filter=1&start=0&hl=en-US&lr=lang_en&cr=countryUS 200
INFO | primp | response: https://yandex.com/search/site/?text=site%3Apostman.com+hackerone&web=1&searchid=3034414 200
INFO | primp | response: https://search.brave.com/search?q=site%3Apostman.com+hackerone&source=web 429
INFO | primp | response: https://www.mojeek.com/search?q=site%3Apostman.com+hackerone 403
INFO | primp | response: https://search.yahoo.com/search;_ylt=XPwx1ml4W6R9u3_PKXibKsyB;_ylu=c4LkDzb1utZcmTkQQlU-wLFCfP1YgV8obIfNpFgCWZSxgVo?p=site%3Apostman.com+hackerone 200
[
│   {
│   │   'title': 'Security & Vulnerability Reporting | Postman',
│   │   'href': 'https://www.postman.com/trust/security/vulnerability-reporting/',
│   │   'body': 'To get your invite on HackerOne , send us an email to security@postman.com with a summary of the nature of the issue you want to report. You should be the first reporter of the vulnerability.'
│   },
│   {
│   │   'title': 'Trust Center | Postman',
│   │   'href': 'https://www.postman.com/trust/',
│   │   'body': 'You can use our PGP public key to encrypt your communications with us. To report a vulnerability, check out our reporting page on HackerOne . Security researchers should also review our security guidelines and policy for reporting security vulnerabilities through our bug bounty program.'
│   },
│   {
│   │   'title': 'HackerOne | Postman Sherlock',
│   │   'href': 'https://www.postman.com/mushroom-sg/postman-sherlock/request/0xvvpui/hackerone',
│   │   'body': 'Start sending API requests with the HackerOne public request from postman-sherlock on the Postman API Network.'
│   },
│   {
│   │   'title': '1. Visualize GraphQL Vulnerabilities | Documentation - Postman',
│   │   'href': 'https://www.postman.com/devrel/graphql-security-101/documentation/5w7blwo/1-visualize-graphql-vulnerabilities',
│   │   'body': 'Get started with 1. Visualize GraphQL Vulnerabilities documentation from GraphQL Security 101 exclusively on the Postman API Network.'
│   },
│   {
│   │   'title': 'Postman | Postman API Network',
│   │   'href': 'https://www.postman.com/h3hackerone1?view=workspaces',
│   │   'body': 'h3 hackerone . 300+ Profile views. Get to know us. Contributors. h3 hackerone .'
│   },
│   {
│   │   'title': 'Security & Vulnerability Reporting | Postman',
│   │   'href': 'https://web.postman.com/trust/security/vulnerability-reporting/',
│   │   'body': 'You can find more information about the exact details of the program at our HackerOne page .'
│   },
│   {
│   │   'title': 'Postman Security - Compliance, Privacy, & Reliability',
│   │   'href': 'https://web.postman.com/security/',
│   │   'body': 'Postman runs a private bug bounty program with HackerOne .To report a vulnerability, check out our reporting page on HackerOne .'
│   },
│   {
│   │   'title': 'Trust Center | Postman',
│   │   'href': 'https://web.postman.com/trust/',
│   │   'body': 'You can use our PGP public key to encrypt your communications with us. To report a vulnerability, check out our reporting page on HackerOne .'
│   },
│   {
│   │   'title': 'HackerOne | Postman Sherlock | Postman API Network',
│   │   'href': 'https://www.postman.com/winter-star-522387/public/request/bnq13bg/hackerone',
│   │   'body': 'Start sending API requests with the HackerOne public request from Public on the Postman API Network.'
│   },
│   {
│   │   'title': 'Security | Postman Trust Center',
│   │   'href': 'https://www.postman.com/trust/security/',
│   │   'body': 'Bug bounty program We invite anyone to identify and report potential security vulnerabilities in the API Platform. Postman runs a private bug bounty program with HackerOne . Please review our security reporting guidelines and policy.'
│   },
│   {
│   │   'title': 'API Client for REST, SOAP, & GraphQL Queries | Postman',
│   │   'href': 'https://www.postman.com/product/api-client/',
│   │   'body': "Use Postman 's API client to create and save REST, SOAP, and GraphQL queries. Send requests, inspect responses, and easily debug APIs."
│   },
│   {
│   │   'title': 'Add and manage CA and client certificates in Postman',
│   │   'href': 'https://learning.postman.com/docs/sending-requests/authorization/certificates/',
│   │   'body': 'Add a CA certificate To avoid “Self signed certificate” errors when sending requests, add your custom CA certificate to Postman . Turn on the CA certificates toggle. Select the PEM file for your CA certificate. (The PEM file can contain multiple CA certificates.) Add a client certificate To send requests to an API that uses mutual TLS authentication, add your client certificate to Postman ...'
│   },
│   {
│   │   'title': "Ntlm authentication doesn't work - Help Hub - Postman Community",
│   │   'href': 'https://community.postman.com/t/ntlm-authentication-doesnt-work/1955',
│   │   'body': 'Jun 22, 2018 · I’m making a request in postman to an api that uses ntlm authentication, but postman gives up after it receives the initial 401. It never attempts to send any credentials to the server. This is what I see in fiddler: Request: GET [url] HTTP/1.1 Content-Type: application/json User-Agent: PostmanRuntime/7.1.5 Accept: / Host: [host] accept-encoding: gzip, deflate Connection: keep-alive Response ...'
│   },
│   {
│   │   'title': 'Real Time Application Security - Gain Deep Code-Level Insights',
│   │   'href': 'https://www.bing.com/aclick?ld=e8Kxbw90Ov7E3MtMCpw5ZOojVUCUz4QIfvNkaPSSXEAs_mV7yKj3y9h3gOxmXZd9u97gkDuKxCChzH8f_34C94DaOcLu-CBaldvedXZGepYUzKNCex3lnbsLvhU3DTx0rOkjNFgIFZ96X6uq5AACaZGFjFAE4Q9_5KieaziMh96Ucu9FjaN7ee72QC3cp4qNXVYXpiT4ilmE8MopTvvzuv71GCk9w&u=aHR0cHMlM2ElMmYlMmZtb25pdG9yLmx1bmlvLmFpJTJmdjMuMCUyZnRlbXBsYXRlJTNmYWNjaWQlM2QxNjg5NiUyNnVybGRlY29kZSUzZDElMjZrdyUzZGFwcGxpY2F0aW9uJTI1MjBzZWN1cml0eSUyNTIwc2VydmljZXMlMjZtdCUzZHAlMjZudyUzZG8lMjZjcG4lM2Q0MjgzMjkyNDAlMjZkZXZpJTNkYyUyNmRldm0lM2QlMjZsb2NwJTNkMTQ5ODQxJTI2bG9jaSUzZCUyNnBsJTNkJTI2Y3IlM2QlMjZhZHAlM2QlMjZzYWR0JTNkJTI2dXJsJTNkaHR0cHMlMjUzQSUyNTJGJTI1MkZ3d3cuZGF0YWRvZ2hxLmNvbSUyNTJGZGclMjUyRnNlY3VyaXR5JTI1MkZhcHBsaWNhdGlvbi1zZWN1cml0eS1tYW5hZ2VtZW50JTI1MkYlMjUzRnV0bV9zb3VyY2UlMjUzRGJpbmclMjUyNnV0bV9tZWRpdW0lMjUzRHBhaWQtc2VhcmNoJTI1MjZ1dG1fY2FtcGFpZ24lMjUzRGRnLXNlY3VyaXR5LW5hLWFwcHNlYyUyNTI2dXRtX2tleXdvcmQlMjUzRGFwcGxpY2F0aW9uJTI1MjUyMHNlY3VyaXR5JTI1MjUyMHNlcnZpY2VzJTI1MjZ1dG1fbWF0Y2h0eXBlJTI1M0RwJTI1MjZpZ2FhZyUyNTNEMTI5NzQyNDg3NjM4NTgyNiUyNTI2aWdhYXQlMjUzRCUyNTI2aWdhY20lMjUzRDQyODMyOTI0MCUyNTI2aWdhY3IlMjUzRCUyNTI2aWdha3clMjUzRGFwcGxpY2F0aW9uJTI1MjUyMHNlY3VyaXR5JTI1MjUyMHNlcnZpY2VzJTI1MjZpZ2FtdCUyNTNEcCUyNTI2aWdhbnQlMjUzRG8lMjUyNnV0bV9jYW1wYWlnbmlkJTI1M0Q0MjgzMjkyNDAlMjUyNnV0bV9hZGdyb3VwaWQlMjUzRDEyOTc0MjQ4NzYzODU4MjYlMjZtc2Nsa2lkJTNkNjFkZmQ1ZTBjZjdjMTM0NGRmMzdiYzY1ZjI5YzdlZjE&rlid=61dfd5e0cf7c1344df37bc65f29c7ef1',
│   │   'body': 'Align DevOps & Security Teams w/ Full Observability Data In 1 Platform. Watch A Demo Today. Detect OWASP Attacks Out Of The Box, Including SSRFs, SQL Injections, XSS Attacks, & More.'
│   },
│   {
│   │   'title': 'Web App Risk Assessment - API Security. Reinforced',
│   │   'href': 'https://www.bing.com/aclick?ld=e8tKZQ6pOvW9mDFS_EjqJ8IjVUCUxgAnfmY2DFR2-YPRrZc_quTiCS-ZaclW4E_a0j1hWxhiFwQGuv81k6qHZJtWaENPuM_dbGGeFcOowmbQWyPoK6bg1UlJ-6Pvk6i1W0R5WBu0PlcaprgC4JOTJz6r_opGEesyA4QNiaQMkN2E_rshAKqThmi4v9tgaX3Np0QrDD6TXIz7qKkhpvPC00a7KWrzA&u=aHR0cHMlM2ElMmYlMmZ3d3cucmVkc2VudHJ5LmNvbSUyZndlYi1hcHBsaWNhdGlvbi1wZW5ldHJhdGlvbi10ZXN0aW5nJTNmdXRtX3Rlcm0lM2Rzb2Z0d2FyZSUyNTIwYXBwbGljYXRpb24lMjUyMHNlY3VyaXR5JTI2dXRtX2NhbXBhaWduJTNkV2ViJTJiQXBwJTJiJTI1MkIlMmJTT0MlMmIyJTJiUGVudGVzdGluZyUyYihUZXN0KSUyNnV0bV9zb3VyY2UlM2RiaW5nJTI2dXRtX21lZGl1bSUzZHBwYyUyNmhzYV9hY2MlM2Q4MjgyMTM0MjkwJTI2aHNhX2NhbSUzZDIzMjc5Nzg4OTg5JTI2aHNhX2dycCUzZDEyMzY5NTE4Nzk4NDI1MDclMjZoc2FfYWQlM2QlMjZoc2Ffc3JjJTNkbyUyNmhzYV90Z3QlM2Rrd2QtNzczMDk5NDkxMTI0NzUlM2Fsb2MtOTAlMjZoc2Ffa3clM2Rzb2Z0d2FyZSUyNTIwYXBwbGljYXRpb24lMjUyMHNlY3VyaXR5JTI2aHNhX210JTNkcCUyNmhzYV9uZXQlM2RhZHdvcmRzJTI2aHNhX3ZlciUzZDMlMjZtc2Nsa2lkJTNkMTc4MjY5ZTZjOTliMWQwOWEwYzYwMDYzZjQ3YjRhYzY&rlid=178269e6c99b1d09a0c60063f47b4ac6',
│   │   'body': 'Our web app testing covers OWASP top 10 vulnerabilities and beyond for your security. Strengthen your SaaS and cloud app security with deep, human-led web app testing.'
│   }
]
```
