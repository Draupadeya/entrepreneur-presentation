from django.shortcuts import render, Http404
import json


def index(request):
    data = {
        "pepper": {
            "name": "PepperTap",
            "stat": "₹130 Loss",
            "stat_label": "Per Order",
            "reason": "Hyper-growth without profit. Scaled to 17 cities in 1 year but lost money on every delivery.",
            "color": "#ef4444",
            "slug": "peppertap"
        },
        "walmart": {
            "name": "Walmart",
            "stat": "$648B",
            "stat_label": "Annual Revenue",
            "reason": "Efficiency through scale. Direct sourcing from manufacturers and 'Everyday Low Prices' strategy.",
            "color": "#3b82f6",
            "slug": "walmart"
        }
    }
    compare = {
        'left': {
            'slug': data['pepper']['slug'],
            'name': data['pepper']['name'],
            'logo': '/static/peppertap_logo.png',
            'tag': 'Hyperlocal marketplace — rapid expansion, negative unit economics',
            'metrics': [
                {'label': 'Scale (cities)', 'value': '17 (peak)'} ,
                {'label': 'Unit economics', 'value': 'Negative per order'},
                {'label': 'Primary risk', 'value': 'High last-mile cost'}
            ],
            'lessons': [
                'Validate contribution margin before geographic scale',
                'Avoid blanket discounts that hide unit economics'
            ]
        },
        'right': {
            'slug': data['walmart']['slug'],
            'name': data['walmart']['name'],
            'logo': '/static/walmart_logo.png',
            'tag': 'Retail scale + supply-chain leverage — cost advantage at volume',
            'metrics': [
                {'label': 'Scale (stores)', 'value': '10,000+'},
                {'label': 'Unit economics', 'value': 'Positive at scale'},
                {'label': 'Primary strength', 'value': 'Logistics & procurement'}
            ],
            'lessons': [
                'Leverage physical network as fulfillment nodes',
                'Invest in telemetry and repeatable supply-chain ops'
            ]
        }
    }

    return render(request, 'index.html', {'data': data, 'compare': compare})


def detail(request, company):
    # Prepare simple, realistic sample datasets for charts.
    company = company.lower()
    if company in ("peppertap", "pepper"):
        meta = {
            "name": "PepperTap",
            "overview": "A hyperlocal grocery/delivery startup that scaled rapidly but suffered negative unit economics: large discounts, high logistics cost and thin commissions.",
            "color": "#ef4444",
            "logo": "/static/peppertap_logo.png",
        }


        timeline = [
            {"date": "Nov 2014", "text": "Launch in Gurgaon."},
            {"date": "Oct 2015", "text": "Peak hyper-growth: expanded to 17 cities; raised $51M."},
            {"date": "Feb 2016", "text": "Cut operations in 10 major cities to save cash."},
            {"date": "Apr 2016", "text": "Grocery delivery operations halted (total shutdown)."}
        ]

        # Structured profile metadata and rich HTML sections (from user's content)
        profile = {
            "Name": "PepperTap",
            "Industry": "Food & Bevarage",
            "Country": "India",
            "Started in": "2014",
            "Outcome": "Shut Down",
            "Cause": "Lack of vision and focus",
            "Closed in": "2016",
            "Employees": "0-25",
            "Funding Rounds": "4",
            "Funding Raised": "$51 Million",
            "Investors": "8",
        }

        sections = [
            {"id":"overview","title":"Overview","html":
                                "<div style='display:flex;gap:14px;align-items:flex-start'>\
                                        <img src='/static/peppertap_founder.png' alt='PepperTap founders' style='width:220px;height:auto;border-radius:8px;box-shadow:0 8px 20px rgba(2,6,23,0.45)'>\
                                        <div>\
                                            <p><strong>What was PepperTap?</strong><br>PepperTap was once India's 3rd biggest online grocery delivery service. Founded by Milind Sharma and Navneet Singh in Gurugram (2014), the startup aimed to deliver groceries in a couple of hours by partnering with local stores.</p>\
                                            <p>The product emphasized speed and convenience: tight SLAs for delivery, an easy app experience, and aggressive promotions to drive trial. Early customers loved the convenience, which helped the company scale order volume rapidly across multiple cities.</p>\
                                        </div>\
                                 </div>"
            },
            {"id":"model","title":"PepperTap's Business Model","html":
                "<p>PepperTap operated as an intermediary between local grocery stores and households, promising 2-hour deliveries with an inventory-less, hyper-local model. They charged ~20% commission from retailers while offering heavy discounts and free delivery to customers.</p><p>The model relied on tight coordination with partner stores and a distributed rider network. Profitability required high repeat purchase rates, strong average order values, and efficient routing; any gap in these metrics increased the per-order subsidy the company had to bear.</p>"
            },
            {"id":"reception","title":"How was PepperTap received?","html":
                "<p>Investors were bullish: within a year PepperTap raised large funds (eventually ~$51M) and expanded aggressively to 17–25 cities. Daily orders peaked near ~20,000 and the company grew headcount rapidly.</p><p>Market response included strong initial retention among frequent shoppers, especially in dense urban pockets. However, expansion into lower-density cities revealed higher logistics and marketing cost per order, making some new markets much more expensive to serve.</p>"
            },
            {"id":"collapse","title":"What happened to PepperTap?","html":
                "<p>While GMV and orders grew, unit economics were negative. After aggressive expansion and mounting losses, PepperTap shut down operations in many cities in early 2016 and finally halted grocery delivery in April 2016.</p><p>Operationally, the company struggled to keep delivery costs under control while paying for acquisition and discounts. Cash constraints forced rapid retrenchment; closing markets reduced revenue but did not immediately eliminate fixed commitments like leases and certain staffing costs.</p>"
            },
            {"id":"reasons","title":"Why did PepperTap fail?","html":
                                "<h3 style='margin-top:0.25rem'>REASONS FOR ITS FAILURE</h3>\
                                <ul>\
                                    <li><strong>Unsustainable Discounts:-</strong> The company spent heavily on promotions and discounts, often selling items at prices below store cost to drive trial. This drove high customer acquisition but resulted in negative contribution per order. E.g. Flat Rs.150 Off on Rs.250 Orders + Extra Rs.100 Referral Bonus.</li>\
                                    <li><strong>Inventory Management:-</strong> PepperTap operated with minimal inventory buffers compared to larger rivals, which increased stockouts and fulfillment friction when partner stores were unable to meet orders.</li>\
                                </ul>\
                                <p style='margin-top:0.5rem'>Additional operational symptoms:</p>\
                                <ul>\
                                    <li>Cash burn due to heavy discounts per order.</li>\
                                    <li>Insufficient buffer capacity in logistics to reliably meet 2-hour SLAs.</li>\
                                </ul>\
                                <div style='display:flex;gap:12px;margin-top:1rem;flex-wrap:wrap'>\
                                      <img src='/static/peppertap_van.png' alt='PepperTap van' style='width:48%;border-radius:6px;box-shadow:0 6px 18px rgba(2,6,23,0.5)'>\
                                      <img src='/static/peppertap_promo.png' alt='PepperTap promo' style='width:48%;border-radius:6px;box-shadow:0 6px 18px rgba(2,6,23,0.5)'>\
                                </div>\
                                <p style='margin-top:0.8rem'>These operational choices — deep discounts, low inventory buffers, and rapid geographic expansion — combined to create unsustainable unit economics and ultimately forced retrenchment.</p>"
            },
            {"id":"next","title":"What happened next?","html":
                "<p>PepperTap’s parent (Nuvo Logistics) continued for a while and was later sold; PepperTap founders moved on and the market learned lessons about quick-delivery economics.</p><p>The episode influenced later entrants to focus earlier on unit economics, hybrid inventory approaches, and tighter geographic rollouts. Some learnings fed into later micro-fulfillment and dark-store experiments that balance speed with inventory control.</p>"
            },
            {"id":"lessons","title":"What do we learn?","html":
                "<ul><li>Build an MVP and validate unit economics before scaling.</li><li>Fast growth without profitability is risky; test retention and repeat purchase economics first.</li><li>Operational quality and inventory control are critical for grocery; strong store partnerships and reliable fulfillment are non-negotiable.</li><li>Consider hybrid inventory models (small local buffers) to reduce last-mile costs without full warehousing investment.</li></ul>"
            }
        ]
    elif company == "walmart":
        meta = {
            "name": "Walmart",
            "overview": "A global retail giant that focused on scale, supply-chain efficiencies and low pricing to drive growth.",
            "color": "#3b82f6",
            "logo": "/static/walmart_logo.png",
        }
        # Rich article sections for Walmart
        sections = [
            {"id": "overview", "title": "Overview — Walmart's Success Story", "html":
                                "<div style='display:flex;gap:14px;align-items:flex-start'>\
                                        <img src='/static/walmart_founder.png' alt='Walmart founder' style='width:220px;height:auto;border-radius:8px;box-shadow:0 8px 20px rgba(2,6,23,0.45)'>\
                                        <div>\
                                            <p>Walmart grew from a single discount store into a global retail leader by obsessing over cost, distribution efficiency and customer value. Its 'Everyday Low Prices' strategy, combined with massive scale, allowed Walmart to win market share across groceries, general merchandise and wholesale.</p>\
                                            <p>The company's playbook—low prices, broad assortment, and operational discipline—turned Walmart into a durable competitive force in retail. Over time Walmart layered on capabilities (private labels, club formats, and marketplace partners) that expanded margin and customer reach while keeping price leadership intact.</p>\
                                            <p>Walmart’s approach balanced close supplier relationships, tight inventory disciplines and continuous reinvestment of operating leverage into better distribution and lower consumer prices. That combination made the model hard for smaller competitors to replicate at scale.</p>\
                                        </div>\
                                 </div>"
            },
            {"id": "timeline", "title": "Growth Timeline — Key Milestones", "html":
                "<ol><li><strong>1962:</strong> Sam Walton opens the original discount store in Rogers, Arkansas.</li><li><strong>1970s–1980s:</strong> Rapid U.S. expansion and development of regional distribution centers that scaled store replenishment.</li><li><strong>1990s–2000s:</strong> International expansion and introduction of Sam's Club; major investments in logistics and IT.</li><li><strong>2010s–2020s:</strong> Digital acceleration: marketplace growth, targeted acquisitions and omnichannel fulfillment (BOPIS, curbside, same-day).</li></ol><p>Each milestone reflects a deliberate choice to reinvest operating leverage into capabilities that reinforce price, convenience and assortment. Over time the company adapted store formats and services to local markets, testing innovations at scale before wider rollout.</p>"
            },
            {"id": "scale", "title": "Scale & Operational Levers", "html":
                "<p>Walmart's scale produces negotiating leverage with suppliers and lets the company amortize significant fixed costs (warehousing, IT, transportation) across huge sales volumes. Scale also enables experiments like private-label programs and regional assortments that increase margins while preserving low consumer prices.</p><ul><li><strong>Procurement:</strong> centralized buying and vendor programs secure consistent pricing and service levels.</li><li><strong>Assortment:</strong> the mix of national brands, private labels and marketplace sellers widens choice without taking full inventory risk.</li><li><strong>Cost absorption:</strong> logistics and IT costs fall per unit as volume rises, funding continuous investment into efficiency.</li></ul><p>Scale also supports product and format experimentation: a successful pilot can be rolled out nationally with predictable economics, which accelerates innovation while dampening execution risk.</p>"
            },
            {"id": "supplychain", "title": "Supply-chain Innovations", "html":
                "<p>Walmart pioneered operational techniques that transformed grocery and general merchandise logistics. Early adoption of barcoding, regional distribution centers, and cross-docking reduced handling time and inventory levels. Later investments in replenishment algorithms and vendor metrics improved fill rates and reduced out-of-stocks.</p><p>Operational excellence allowed Walmart to lower per-unit cost and pass savings to customers — a virtuous loop that reinforced competitiveness. The company’s focus on logistics extended to private trucking fleets, automated sortation centers and investments in warehouse geography to cut transit time to stores.</p>"
            },
            {"id": "digital", "title": "Digital Transformation & Omnichannel", "html":
                "<p>Walmart's digital strategy is pragmatic and store-centric: rather than replace stores, it augmented them into fulfillment nodes. Curbside pickup, buy-online-pickup-in-store (BOPIS), and same-day delivery pilots make stores part of the fulfillment footprint, reducing last-mile costs and improving delivery speed.</p><p>Marketplace expansion lets Walmart offer far more SKUs without owning inventory, while partnerships and selective acquisitions brought new tooling and talent to accelerate e-commerce capabilities. Integrating store inventory with online search and checkout created an omnichannel experience that leverages physical real estate as a competitive asset.</p>"
            },
            {"id": "technology", "title": "Technology & Data (How Walmart Scales Intelligence)", "html":
                "<p>Walmart invested heavily in engineering and data platforms to scale intelligence across pricing, assortment and logistics. In-house teams built services for search, personalization and forecasting. Practical technologies—demand forecasting, route optimization, automated replenishment—convert scale into lower costs and improved availability.</p><p>Data-driven pricing and promotion systems allow Walmart to react to competitors while protecting margins where possible. The company also invests in analytics for category management, customer behavior and supply chain telemetry so decisions are driven by observed operational signals rather than intuition.</p>"
            },
            {"id": "acquisitions", "title": "Strategic Acquisitions & Partnerships", "html":
                "<p>Targeted acquisitions and partnerships helped Walmart accelerate into adjacent capabilities—marketplace operations, last-mile logistics, fintech and cloud tooling. These moves brought specialized teams and platforms that shortened time-to-market for valuable customer experiences.</p><p>Strategic M&A and investments are used to bring new channels, talent and platform capabilities into the company quickly, while partnerships fill capability gaps without heavy upfront investment.</p>"
            },
            {"id": "sustainability", "title": "Sustainability as a Business Lever", "html":
                "<p>Walmart framed sustainability (supplier engagement, energy efficiency, waste reduction) as both responsibility and operational opportunity. Programs that lower energy and waste across the supply chain can also reduce operating costs and strengthen supplier relationships.</p><p>By setting supplier goals and investing in energy-efficient stores and fleets, Walmart treats sustainability as part of long-term cost management and resilience planning. Sustainability efforts also support brand trust with customers and regulators.</p>"
            },
            {"id": "lessons", "title": "Why It Worked — Key Lessons", "html":
                "<ul><li>Relentless focus on operational efficiency creates a durable cost advantage.</li><li>Using physical assets (stores, clubs) as part of omnichannel fulfillment increases flexibility and lowers last-mile cost.</li><li>Investing in technology and partnerships shortens time-to-market for new customer experiences.</li><li>Tactical acquisitions and marketplace models let Walmart scale assortment without full inventory exposure.</li><li>Continuous reinvestment of operating leverage into logistics and data capabilities sustains competitive advantage over the long run.</li></ul>"
            }
        ]
    else:
        raise Http404()

    comparison = [
        {"metric": "Business Model", "pepper": "Hyperlocal marketplace, heavy delivery subsidy", "walmart": "Retail + wholesale, vertical integration"},
        {"metric": "Scale", "pepper": "~17 cities (peak)", "walmart": "~10,000+ stores worldwide"},
        {"metric": "Unit Economics", "pepper": "Negative contribution per order", "walmart": "Positive at scale"},
        {"metric": "Primary Downfall/Success Driver", "pepper": "Burn rate + unsustainable subsidies", "walmart": "Supply chain efficiency + pricing"}
    ]
    context = {
        'company': meta,
        'comparison': comparison,
    }

    # pepper timeline only; for walmart we pass an empty timeline (could add milestones later)
    if company in ("peppertap", "pepper"):
        context['timeline'] = timeline
    else:
        context['timeline'] = [
            {"date": "1962", "text": "Founded (Sam Walton) - long history of scaling retail."},
            {"date": "2000s", "text": "Massive supply-chain investments and global expansion."}
        ]

    # Render template specific to company. Use the unified presentation (walmart.html) for both companies so
    # PepperTap uses the same UI as Walmart. Templates receive `company` and `sections` in context.
    context['sections'] = sections
    if company in ("peppertap", "pepper", "walmart"):
        return render(request, 'walmart.html', context)
    else:
        return render(request, 'presentation.html', context)