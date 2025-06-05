# Ukrainian Business Map — Valencia 🇺🇦📍

This is a community-driven map of Ukrainian-owned or Ukrainian-run businesses in Valencia, Spain.

The goal is to help our local Ukrainian IT community discover, support, and connect with trusted businesses.

> 🛑 **Important:** This repository is intended for internal use by the Ukrainian IT Community in Valencia. Do not reuse, redistribute, or embed this dataset or map without explicit permission. All rights reserved.

---

## 🗺 Live map

Coming soon via GitHub Pages  
(example: https://map.pizd.es)

---

## 📁 How to contribute

We use a public JSON file to store business listings. You can suggest additions or corrections via Pull Request.

### Steps:
1. Fork this repo
2. Edit [`data/businesses.json`](data/businesses.json)
3. Follow the format shown below
4. Open a Pull Request — once approved by 2 members, it will be merged automatically

### Example:
```json
{
  "name": "Кав'ярня «Доброго Ранку»",
  "category": "Кафе та ресторани",
  "location": { "lat": 39.4712, "lng": -0.3768 },
  "address": "Carrer de Xàtiva, 12, Valencia",
  "contact": "+34 612 345 678",
  "instagram": "https://instagram.com/example",
  "maps_url": "https://maps.app.goo.gl/example"
}
