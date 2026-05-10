import pandas as pd


retail_summary = {
    "total_spend": 267371.94,
    "total_purchase": 113,
    "total_revenue": 1635440,
    "total_reach": 1346685,
    "total_impressions": 3866121,
    "avg_roas": 6.12,
    "avg_cpr": 2366.12,
    "avg_ctr_click": 1.62,
}

retail_data = pd.DataFrame([
    {"Campaign": "CP 1", "Spend": 3767.21, "Revenue": 8721, "Purchase": 1, "CPR": 3767.21, "ROAS": 1.005519, "CTR Click": 2.716998, "CPM": 104.871945, "Frequency": 1.801956},
    {"Campaign": "CP2 Retarget", "Spend": 1123.96, "Revenue": 64396, "Purchase": 4, "CPR": 280.99, "ROAS": 54.4708, "CTR Click": 4.035513, "CPM": 129.59299, "Frequency": 1.73356},
    {"Campaign": "CP 3", "Spend": 57971.25, "Revenue": 260603, "Purchase": 31, "CPR": 2147.08333333, "ROAS": 4.495383, "CTR Click": 1.061289, "CPM": 70.450328, "Frequency": 3.855261},
    {"Campaign": "CP 4 Retarget", "Spend": 20500.00, "Revenue": 120996, "Purchase": 10, "CPR": 2050.0, "ROAS": 5.902244, "CTR Click": 3.299395, "CPM": 93.849859, "Frequency": 3.90005},
    {"Campaign": "CP 5", "Spend": 19999.79, "Revenue": 15900, "Purchase": 1, "CPR": 19999.79, "ROAS": 0.795008, "CTR Click": 1.258394, "CPM": 143.486986, "Frequency": 3.061904},
    {"Campaign": "CP 6", "Spend": 20000.00, "Revenue": 23796, "Purchase": 2, "CPR": 10000.0, "ROAS": 1.1898, "CTR Click": 0.860837, "CPM": 64.241548, "Frequency": 2.558576},
    {"Campaign": "CP 7", "Spend": 4997.85, "Revenue": 45121, "Purchase": 2, "CPR": 2498.925, "ROAS": 9.028082, "CTR Click": 0.695057, "CPM": 133.607346, "Frequency": 2.784709},
    {"Campaign": "CP 8", "Spend": 29994.23, "Revenue": 283350, "Purchase": 13, "CPR": 2726.74818182, "ROAS": 9.446817, "CTR Click": 1.442813, "CPM": 52.058313, "Frequency": 2.765787},
    {"Campaign": "CP 9", "Spend": 25494.69, "Revenue": 291325, "Purchase": 17, "CPR": 1593.418125, "ROAS": 11.426889, "CTR Click": 1.080882, "CPM": 53.466706, "Frequency": 2.664839},
    {"Campaign": "CP 10", "Spend": 1828.19, "Revenue": 24846, "Purchase": 1, "CPR": 1828.19, "ROAS": 13.590491, "CTR Click": 1.339488, "CPM": 69.176252, "Frequency": 2.301088},
    {"Campaign": "CP 11", "Spend": 47746.11, "Revenue": 378089, "Purchase": 19, "CPR": 2808.59470588, "ROAS": 7.918739, "CTR Click": 1.281042, "CPM": 58.009076, "Frequency": 4.08286},
    {"Campaign": "CP 12", "Spend": 11737.26, "Revenue": 61707, "Purchase": 7, "CPR": 1676.75142857, "ROAS": 5.25736, "CTR Click": 1.435302, "CPM": 51.205218, "Frequency": 2.183859},
    {"Campaign": "CP 13", "Spend": 22210.44, "Revenue": 51789, "Purchase": 3, "CPR": 7403.48, "ROAS": 2.331741, "CTR Click": 1.222362, "CPM": 39.919408, "Frequency": 3.426609},
])
