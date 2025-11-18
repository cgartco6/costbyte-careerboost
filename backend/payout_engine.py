def split_revenue(amount):
    return {
        "owner_fnb_40": amount * 0.40,
        "owner_african_20": amount * 0.20,
        "reserve_fnb_20": amount * 0.20,
        "ai_fund_fnb_20": amount * 0.20
    }
