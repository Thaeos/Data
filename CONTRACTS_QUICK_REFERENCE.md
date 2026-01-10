# Quick Reference: 22 Contract Addresses
## The Complete Registry (𐡀-𐡕)

**Network**: Arbitrum One (ChainID: 42161)  
**Date**: 7 Balance 2, Year 5250

---

## VERIFIED ADDRESSES (Copy-Paste Ready)

### Foundation Layer (1-5):
```
1.  𐡀 MAGIC               0x539bdE0d7Dbd336b79148AA742883198BBF60342
2.  𐡁 Treasure            0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18326
3.  𐡂 TreasureFarm        0x83a19AE12B07D82Df1b7AB63E2b0a75EaAfC9c97
4.  𐡃 MagicPool2          [Pending verification]
5.  𐡄 TreasureUnraveler   [Pending verification]
```

### Operational Layer (6-18):
```
6.  𐡅 MagicClaim          [Pending verification]
7.  𐡆 Cards               [Pending verification]
8.  𐡇 MagicWhitelist      [Pending verification]
9.  𐡈 TreasureMarketplace 0x09986B4e255B3c548041a30A2Ee312Fe176731c2
10. 𐡉 MarketplaceBuyer    [Facet of Marketplace]
11. 𐡊 MarketplaceSeller   [Facet of Marketplace]
12. 𐡋 MagicswapV2Router   [Pending verification]
13. 𐡌 MagicswapV2Factory  [Pending verification]
14. 𐡍 MagicswapV2Pair     [Pending verification]
15. 𐡎 Legion              0xfE8c1ac365bA6780AEc5a985D989b327C27670A1
16. 𐡏 Consumable          0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18327
17. 𐡐 Harvester           [Pending verification]
18. 𐡑 Extractor           [Pending verification]
```

### Governance Layer (19-22):
```
19. 𐡒 BalancerCrystal     [Pending verification]
20. 𐡓 gMAGIC              [Pending verification]
21. 𐡔 TreasureDAO         [Pending verification]
22. 𐡕 ZKStackBridge       [Pending verification]
```

---

## MASTER KEY HASHES

```
Master Hash:    69f7ddaab06f2c2e0259729b188f0c922658a1aacde1d9a307aaba26ff9df71e
Signer Hash:    883e529de31c586131a831a9953113a6d75edd87c97369a2fa3a791209952f5a
PGP Fingerprint: 0xe45398c60bbde43806212e323515c3cc041fe17e
```

---

## JSON FORMAT (For Code Integration)

```json
{
  "network": {
    "name": "Arbitrum One",
    "chainId": 42161,
    "rpc": "https://arb1.arbitrum.io/rpc",
    "explorer": "https://arbiscan.io"
  },
  "contracts": {
    "foundation": {
      "1_MAGIC": {
        "address": "0x539bdE0d7Dbd336b79148AA742883198BBF60342",
        "glyph": "𐡀",
        "identity": 82,
        "verified": true
      },
      "2_Treasure": {
        "address": "0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18326",
        "glyph": "𐡁",
        "identity": 111,
        "verified": true
      },
      "3_TreasureFarm": {
        "address": "0x83a19AE12B07D82Df1b7AB63E2b0a75EaAfC9c97",
        "glyph": "𐡂",
        "identity": 212,
        "verified": false
      }
    },
    "operational": {
      "9_TreasureMarketplace": {
        "address": "0x09986B4e255B3c548041a30A2Ee312Fe176731c2",
        "glyph": "𐡈",
        "identity": 512,
        "verified": true
      },
      "15_Legion": {
        "address": "0xfE8c1ac365bA6780AEc5a985D989b327C27670A1",
        "glyph": "𐡎",
        "identity": 1011,
        "verified": true
      },
      "16_Consumable": {
        "address": "0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18327",
        "glyph": "𐡏",
        "identity": 2025,
        "verified": true
      }
    }
  },
  "masterKey": {
    "masterHash": "69f7ddaab06f2c2e0259729b188f0c922658a1aacde1d9a307aaba26ff9df71e",
    "signerHash": "883e529de31c586131a831a9953113a6d75edd87c97369a2fa3a791209952f5a",
    "pgpFingerprint": "0xe45398c60bbde43806212e323515c3cc041fe17e"
  }
}
```

---

## ETHERS.JS INTEGRATION

```javascript
const contracts = {
  MAGIC: '0x539bdE0d7Dbd336b79148AA742883198BBF60342',
  Treasure: '0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18326',
  TreasureFarm: '0x83a19AE12B07D82Df1b7AB63E2b0a75EaAfC9c97',
  TreasureMarketplace: '0x09986B4e255B3c548041a30A2Ee312Fe176731c2',
  Legion: '0xfE8c1ac365bA6780AEc5a985D989b327C27670A1',
  Consumable: '0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18327'
};

// Load contract
const provider = new ethers.JsonRpcProvider('https://arb1.arbitrum.io/rpc');
const magic = new ethers.Contract(contracts.MAGIC, magicABI, provider);
```

---

## WEB3.PY INTEGRATION

```python
from web3 import Web3

# Connect to Arbitrum
w3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))

# Contract addresses
MAGIC_ADDRESS = '0x539bdE0d7Dbd336b79148AA742883198BBF60342'
TREASURE_ADDRESS = '0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18326'
MARKETPLACE_ADDRESS = '0x09986B4e255B3c548041a30A2Ee312Fe176731c2'
LEGION_ADDRESS = '0xfE8c1ac365bA6780AEc5a985D989b327C27670A1'
CONSUMABLE_ADDRESS = '0xf3dF4A0cCD4C6C39c0828B89D22DA5A0c6B18327'

# Load contract
magic = w3.eth.contract(address=MAGIC_ADDRESS, abi=magic_abi)
balance = magic.functions.balanceOf(wallet_address).call()
```

---

## CURRENT STATUS

**Date**: 7 Balance 2, Year 5250  
**Active Contract**: #12 (MagicswapV2Router / 777)  
**Active Kingdom**: Middle (BalancerCrystal / 5250)

**Verified**: 6/22 contracts (27%)  
**Pending**: 16/22 contracts (73%)

---

**∇ • Θεός°●⟐●Σ℧ΛΘ**
