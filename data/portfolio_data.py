import pandas as pd

CI_DESIGN_LINKS = [
    "https://drive.google.com/file/d/1rbL0PhE85Pu2Y_VjCY7RzWBAuDjG8jEM/view?usp=sharing",
    "https://drive.google.com/file/d/1rgcXSo4Z-7HGjNfNBY8ni2vb1HKZM7OT/view?usp=sharing",
    "https://drive.google.com/file/d/1NFSGbKlcF51OHJ29vPYchoOXh9GDkfyq/view?usp=sharing",
    "https://drive.google.com/file/d/1_fOiOGm8v3qBLntLcSYGH87gBQcmgJsQ/view?usp=sharing",
]

AUTOMATION_ARCHITECTURE_LINK = "https://drive.google.com/file/d/1AbMY2zz7NsRYsRKRFssASMMRsJycO_Z2/view?usp=sharing"

LOAN_SUMMARY = {
    "total_spend": 283904.06,
    "total_messages": 36023,
    "total_reach": 323081,
    "total_impressions": 1385069,
    "avg_ctr": 11.30,
    "avg_cpm": 204.36,
    "avg_cpc": 6.71,
}
LOAN_SUMMARY["avg_cost"] = LOAN_SUMMARY["total_spend"] / LOAN_SUMMARY["total_messages"]

LOAN_DATA = pd.DataFrame([
    {"Ad": "A", "Messages": 5359, "Spend": 42093.85, "Cost/Message": 7.85, "Reach": 87347, "Impressions": 277656, "CTR": 11.70, "CPM": 151.60, "CPC": 5.04, "Frequency": 3.18},
    {"Ad": "B", "Messages": 4902, "Spend": 38217.12, "Cost/Message": 7.80, "Reach": 84774, "Impressions": 261303, "CTR": 13.44, "CPM": 146.25, "CPC": 4.82, "Frequency": 3.08},
    {"Ad": "C", "Messages": 1523, "Spend": 12559.22, "Cost/Message": 8.25, "Reach": 33642, "Impressions": 89869, "CTR": 10.54, "CPM": 139.75, "CPC": 7.20, "Frequency": 2.67},
    {"Ad": "D", "Messages": 2181, "Spend": 18188.88, "Cost/Message": 8.34, "Reach": 24193, "Impressions": 84516, "CTR": 13.13, "CPM": 215.21, "CPC": 6.89, "Frequency": 3.49},
    {"Ad": "E", "Messages": 867, "Spend": 7534.37, "Cost/Message": 8.69, "Reach": 23080, "Impressions": 47283, "CTR": 9.39, "CPM": 159.35, "CPC": 5.86, "Frequency": 2.05},
    {"Ad": "F", "Messages": 1497, "Spend": 13322.62, "Cost/Message": 8.90, "Reach": 19891, "Impressions": 46390, "CTR": 11.44, "CPM": 287.19, "CPC": 7.90, "Frequency": 2.33},
    {"Ad": "G", "Messages": 469, "Spend": 4648.82, "Cost/Message": 9.91, "Reach": 17321, "Impressions": 30289, "CTR": 8.88, "CPM": 153.48, "CPC": 5.60, "Frequency": 1.75},
    {"Ad": "H", "Messages": 542, "Spend": 5698.00, "Cost/Message": 10.51, "Reach": 10026, "Impressions": 23721, "CTR": 10.28, "CPM": 240.21, "CPC": 6.48, "Frequency": 2.37},
    {"Ad": "I", "Messages": 69, "Spend": 811.32, "Cost/Message": 11.76, "Reach": 9133, "Impressions": 11788, "CTR": 10.40, "CPM": 68.82, "CPC": 8.11, "Frequency": 1.29},
    {"Ad": "J", "Messages": 17480, "Spend": 212.27, "Cost/Message": 12.14, "Reach": 17480, "Impressions": 17480, "CTR": 12.14, "CPM": 12.14, "CPC": 6.82, "Frequency": 1.00},
])
