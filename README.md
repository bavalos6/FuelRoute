# ⛽ FuelRoute — Road Trip Gas Estimator

A single-page web app that calculates your estimated gas cost for any road trip across the US. No build tools, no dependencies to install — just open `index.html` or deploy to GitHub Pages.

![FuelRoute Screenshot](https://via.placeholder.com/900x500/0c0f0a/b4d264?text=FuelRoute+App)

## Features

- **Route planning** — Finds the best driving route between any two US cities using OpenRouteService
- **Vehicle lookup** — Search your car by Year/Make/Model using the NHTSA + EPA FuelEconomy.gov APIs (no API key needed)
- **Manual MPG** — Or just enter your car's MPG directly
- **Fuel type** — Regular, Mid-Grade, Premium, or Diesel pricing
- **State-by-state breakdown** — See how much you'll spend in each state along the route
- **Live gas prices** — Uses EIA (U.S. Energy Information Administration) state average prices
- **Interactive map** — Dark-themed map with your route drawn on it

## APIs Used (all free, no paid key required)

| API | Used For |
|-----|----------|
| [OpenRouteService](https://openrouteservice.org/) | Route calculation & distance |
| [NHTSA vPIC](https://vpic.nhtsa.dot.gov/api/) | Vehicle make/model lookup |
| [EPA FuelEconomy.gov](https://www.fueleconomy.gov/feg/ws/) | MPG data by vehicle |
| [Nominatim (OSM)](https://nominatim.org/) | Address geocoding & autocomplete |
| [EIA](https://www.eia.gov/) | State-level gas price averages (baked in, updated periodically) |
| [CARTO Dark tiles](https://carto.com/basemaps/) | Map tiles |

## Deploy to GitHub Pages (3 steps)

1. **Create a new GitHub repository** (e.g. `fuelroute`)

2. **Upload `index.html`** to the root of the repo (drag & drop in GitHub UI, or via git)

3. **Enable GitHub Pages:**
   - Go to your repo → Settings → Pages
   - Source: `Deploy from a branch`
   - Branch: `main` / `(root)`
   - Click Save

Your app will be live at `https://YOUR_USERNAME.github.io/fuelroute/` within ~60 seconds.

## Run Locally

No build step needed. Just open the file:

```bash
# Option 1: directly in browser
open index.html

# Option 2: local server (avoids some CORS issues)
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Updating Gas Prices

Gas prices are stored in the `STATE_GAS_PRICES` object near the top of the `<script>` section. To update them:

1. Visit [EIA Weekly Retail Gasoline Prices](https://www.eia.gov/petroleum/gasprices/)
2. Download the state-level table
3. Update the values in the `STATE_GAS_PRICES.regular` (and other fuel types) object

## Optional: Live Gas Price API

To replace the static prices with live data, you can integrate:
- [GasBuddy API](https://www.gasbuddy.com/) (paid)
- [CollectAPI Gas Prices](https://collectapi.com/api/gasPrice/gas-prices-api) (freemium)
- [EIA API](https://www.eia.gov/opendata/) (free, but weekly, state-level only)

Replace the `STATE_GAS_PRICES` lookup in `calculateStateCosts()` with a `fetch()` call to your chosen API.

## OpenRouteService API Key

The app uses the public demo key from OpenRouteService. For production use:
1. Sign up free at [openrouteservice.org](https://openrouteservice.org/dev/#/signup)
2. Get your free API key (2,000 req/day free tier)
3. Replace `ORS_KEY` near the top of the script

## License

MIT — use freely, modify as needed.
