# Are there really that many Isekai?
### A Data Analysis by Andrés Ríos 

This project investigates the perceived "saturation" of the Isekai genre within the anime industry. By analyzing historical release data, growth rates (CAGR), and cross-medium correlations with Light Novels, this analysis aims to determine if nowadays are really that many Isekai as one might think. 

## 📂 Project Structure
```text
.
├── data/           # Raw CSV datasets used for the analysis
├── docs/           # Project documentation
│   ├── methodology.md
│   ├── limitations.md
│   ├── isekai.md   # Definition and scope of the genre
│   └── README.md   # Project overview
├── notebooks/      # Jupyter Notebooks containing the data processing and analysis
├── results/        
│   ├── figures/    # Charts and visualizations (PNG/SVG)
│   └── results.md  # Final published analysis and conclusions
└── src/            # Python helper scripts and utility functions
```

## 🛠️ Methodology & Tools
The analysis was performed using **Python** (Pandas, Matplotlib, Numpy) to process industry data from the last 25 years. Key metrics include:

* **CAGR (Compound Annual Growth Rate):** Used to compare the growth of the Isekai sub-genre against general anime industry averages.
* **IQR (Interquartile Range):** Used to identify statistical abnormalities and outliers in sub-genre distribution to determine if Isekai's share is truly "abnormal".
* **Time-Lag Correlation:** A two-year shift was applied to Light Novel data, based on founds by Sho Hasegawa and Masashi Yamada in their statistical anaysis. 

## 📊 Key Findings
* **Exponential Growth:** Isekai releases increased by **1,020%** between the 2000–2004 and 2020–2024 periods.
* **Market Outpace:** With a CAGR of **11.03%**, Isekai is growing nearly twice as fast as the general anime industry at 6.3%.
* **Statistical Context:** Despite its growth, Isekai's market share is not "abnormal" when compared to dominant sub-genres like "School," which shows significantly higher statistical deviation.
* **The Source Engine:** There is a **0.96 correlation** (with a two-year lag) between Light Novel releases and Anime adaptations, suggesting a direct feedback loop between the two industries.

## 📝 Final Conclusion
The perceived "excess" of the Isekai sub-genres is firmly backed by data, since it has seen a 1,020% increase in releases since the early 2000s. With a growth rate nearly double the industry average, the category has successfully transitioned from a niche interest into a dominant market force.

However, while these figures represent a significant statistical surge, this volume is not abnormal when viewed alongside other industry giants. When compared to the School sub-genre it becomes clear that Isekai has not "broken" the industry’s output model. Instead, it has simply ascended to join the top tier of most-produced themes, and up to day Isekai is not the most prevalent among them. 

## 🔗 Data Sources & References
* **Primary Dataset:** [Animes [1962-2024]](https://www.kaggle.com/datasets/youcmoulai/animes) by Youxise
* **Light Novel:** [novel-dataser](https://github.com/shaido987/novel-dataset) by shaido987
* **Manga:** [MyanimeList Anime & Manga Dataset (July 2025)](https://www.kaggle.com/datasets/hamzaashfaque1999/myanimelist-scraped-data) by Hamza Ashfaq
* **Academic Reference:** Hasegawa, S., Yamada, M.  (2023). A Statistical Analysis of History of Japanese Light Novels. 

---
*For a detailed breakdown of the findings, please refer to [results](../results/results.md).*
