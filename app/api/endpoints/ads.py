from fastapi import APIRouter

router = APIRouter()

ADS_CONFIG = {
    "enabled": True,
    "interstitialProvider": "adsterra",  # adsterra | unity
    "rewardedProvider": "adsterra",      # adsterra | unity
    "unity": {
        "gameId": "6045785",
        "testMode": False,
        "placements": {
            "interstitial": {
                "android": "Interstitial_Android",
                "ios": "Interstitial_iOS",
            },
            "rewarded": {
                "android": "Rewarded_Android",
                "ios": "Rewarded_iOS",
            },
        },
    },
    "adsterra": {
        "smartlink": "https://www.profitablecpmratenetwork.com/mez5kqt1w?key=67b9838356652850bc7aa9c9ea0fd84a",
    },
}


@router.get("/ads/config", tags=["Ads"])
async def get_ads_config():
    return {
        "status": "success",
        "data": ADS_CONFIG,
    }
