import pandas as pd


sample = pd.DataFrame([
    {"Campaign": "Loan Lead Gen", "Spend": 42000, "Leads": 186, "Signal": "Chat Intent", "Decision": "Scale Carefully"},
    {"Campaign": "High AOV Retail", "Spend": 68000, "Leads": 124, "Signal": "O2O Store Visit", "Decision": "Optimize Trust"},
    {"Campaign": "Hotel Booking Push", "Spend": 18000, "Leads": 52, "Signal": "Seasonal Demand", "Decision": "Hold / Burst"},
])

loan_meta = pd.DataFrame([
    {"Campaign": "Loan CP 1", "Messages": 4902, "Spend": 38217.12, "Cost / Message": 7.80, "Reach": 84774, "Impressions": 261303},
    {"Campaign": "Loan CP 2", "Messages": 1523, "Spend": 12559.22, "Cost / Message": 8.25, "Reach": 33642, "Impressions": 89869},
    {"Campaign": "Loan CP 3", "Messages": 2181, "Spend": 18188.88, "Cost / Message": 8.34, "Reach": 24193, "Impressions": 84516},
    {"Campaign": "Loan CP 4", "Messages": 867, "Spend": 7534.37, "Cost / Message": 8.69, "Reach": 23080, "Impressions": 47283},
    {"Campaign": "Loan CP 5", "Messages": 1497, "Spend": 13322.62, "Cost / Message": 8.90, "Reach": 19891, "Impressions": 46390},
    {"Campaign": "Loan CP 6", "Messages": 17480, "Spend": 212.27, "Cost / Message": 12.14, "Reach": 17480, "Impressions": 17480},
    {"Campaign": "Loan CP 7", "Messages": 469, "Spend": 4648.82, "Cost / Message": 9.91, "Reach": 17321, "Impressions": 30289},
    {"Campaign": "Loan CP 8", "Messages": 10902, "Spend": 140.64, "Cost / Message": 12.90, "Reach": 10902, "Impressions": 10902},
    {"Campaign": "Loan CP 9", "Messages": 542, "Spend": 5698.00, "Cost / Message": 10.51, "Reach": 10026, "Impressions": 23721},
    {"Campaign": "Loan CP 10", "Messages": 69, "Spend": 811.32, "Cost / Message": 11.76, "Reach": 9133, "Impressions": 11788},
    {"Campaign": "Loan CP 11", "Messages": 322, "Spend": 3443.48, "Cost / Message": 10.69, "Reach": 8020, "Impressions": 15390},
])

appliance_meta = pd.DataFrame([
    {"Campaign": "CP 1", "Spend": 3767.21, "Purchase": 1, "ROAS": 1.01, "CPR": 3767.21, "CTR Click": 2.72, "CPM": 104.87, "Frequency": 1.80},
    {"Campaign": "CP2 Retarget", "Spend": 1123.96, "Purchase": 4, "ROAS": 54.47, "CPR": 280.99, "CTR Click": 4.04, "CPM": 129.59, "Frequency": 1.73},
    {"Campaign": "CP 3", "Spend": 57971.25, "Purchase": 31, "ROAS": 4.50, "CPR": 2147.08, "CTR Click": 1.06, "CPM": 70.45, "Frequency": 3.86},
    {"Campaign": "CP 4 Retarget", "Spend": 20500.00, "Purchase": 10, "ROAS": 5.90, "CPR": 2050.00, "CTR Click": 3.30, "CPM": 93.85, "Frequency": 3.90},
    {"Campaign": "CP 5", "Spend": 19999.79, "Purchase": 1, "ROAS": 0.80, "CPR": 19999.79, "CTR Click": 1.26, "CPM": 143.49, "Frequency": 3.06},
    {"Campaign": "CP 6", "Spend": 20000.00, "Purchase": 2, "ROAS": 1.19, "CPR": 10000.00, "CTR Click": 0.86, "CPM": 64.24, "Frequency": 2.56},
    {"Campaign": "CP 7", "Spend": 4997.85, "Purchase": 2, "ROAS": 9.03, "CPR": 2498.93, "CTR Click": 0.70, "CPM": 133.61, "Frequency": 2.78},
    {"Campaign": "CP 8", "Spend": 29994.23, "Purchase": 13, "ROAS": 9.45, "CPR": 2726.75, "CTR Click": 1.44, "CPM": 52.06, "Frequency": 2.77},
    {"Campaign": "CP 9", "Spend": 25494.69, "Purchase": 17, "ROAS": 11.43, "CPR": 1593.42, "CTR Click": 1.08, "CPM": 53.47, "Frequency": 2.66},
    {"Campaign": "CP 10", "Spend": 1828.19, "Purchase": 1, "ROAS": 13.59, "CPR": 1828.19, "CTR Click": 1.34, "CPM": 69.18, "Frequency": 2.30},
    {"Campaign": "CP 11", "Spend": 47746.11, "Purchase": 19, "ROAS": 7.92, "CPR": 2808.59, "CTR Click": 1.28, "CPM": 58.01, "Frequency": 4.08},
    {"Campaign": "CP 12", "Spend": 11737.26, "Purchase": 7, "ROAS": 5.26, "CPR": 1676.75, "CTR Click": 1.44, "CPM": 51.21, "Frequency": 2.18},
    {"Campaign": "CP 13", "Spend": 22210.44, "Purchase": 3, "ROAS": 2.33, "CPR": 7403.48, "CTR Click": 1.22, "CPM": 39.92, "Frequency": 3.43},
])
