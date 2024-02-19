# Ethereum Whale Tracker 🐋

## Project Overview 🌐
This project is a powerful analytical tool for tracking and analyzing 'whale' activities on the Ethereum blockchain. Using Python and Web3.0 technologies, it integrates with various APIs like Etherscan and CoinMarketCap to monitor large holders ('whales') and their impact on the market.

## Features 🛠️
- **Data Collection:** Connects with APIs to fetch real-time data from the Ethereum blockchain.
- **Whale Tracking:** Monitors the top 100 holders for selected cryptocurrencies.
- **Trade Size Indicator:** Calculates the trade size for different time frames to gauge market movements.
- **Cumulative Volume Delta (CVD):** Provides CVD analysis for individual holders and the top 100 holders over various time frames.
- **Data Visualization:** Utilizes libraries like Matplotlib for graphical representation of data.
- **Data Storage:** Processes and stores data in various formats, including CSV and PNG images.

## Analysis 📊
The project carries out two types of analyses:

### A. Per HOLDER:
1. **Trade Size Indicator** for different time frames.
2. **CVD** for different time frames.

### B. For top 100 HOLDERS:
1. **Trade Size Indicator** for different time frames.
2. **CVD** for different time frames.

## How it Works ⚙️
- **Data Retrieval:** Using Python scripts to pull data from APIs.
- **Data Processing:** Analyzing data using Pandas and visualizing with Matplotlib.
- **Storage:** Saving processed data for review and further analysis.

## Progress and Milestones 🚀
- **Started:** 9/13/2022
- **Week 1 Achievements:**
  - API connection established and top 100 holders' data extracted.
  - Excel file creation for all chosen coin addresses with daily balance updates.
  - Manual entry system for daily data updates.

## Important Notes 📝
- Verify the `get` function in `analyze.py` for proper handling of large numbers.
- Investigate and resolve any issues with specific coins like Ocean.

## Upcoming Features 🔜
- Trade size analysis among the top 100 holders by various time frames.
- Correlation tracking between price movements and holder activities.
- Implementation of linear regression/AI/ML for enhanced data analysis.
- Daily average price API integration or specific day price retrieval.
- Solutions for handling API errors from Etherscan.

## Also in the Pipeline 🌟
- Server hosting on Replit.
- Daily email dispatch with analysis once AI algorithms are in place.

## Contributing 🤝
Feel free to dive in! Open an issue, submit a pull request, or simply suggest improvements.

## License 📄
This project is open-source and available under [insert license type here].

## Contact 📬
For further details or inquiries about the project, reach out via github.

Happy Whale Tracking! 🚀
