# 📖 The Noble Qur'an Dataset (Text, Translations, Tafseer & Word-by-Word)

A production-grade, highly structured, and categorized JSON dataset of the Holy Qur'an designed for mobile apps (Flutter, React Native, iOS, Android) and web platforms.

---

## 🌟 Highlights

- **Standardized Schema**: Clean, validated JSON with consistent key naming and data types.
- **Unified `complete.json` Per Surah**: Every Surah (`surah_001` through `surah_114`) includes a single `complete.json` bundling Arabic text, translations, tafseers, and word-by-word data for instant single-request loading.
- **49 Languages & 106 Translations**: Categorized neatly into language directories (`english/`, `urdu/`, `hindi/`, `french/`, `indonesian/`, `turkish/`, etc.).
- **25 Comprehensive Tafseers**: Classical and contemporary commentaries in Arabic, Urdu, English, and Hindi.
- **6 Arabic Script Types**: Indo-Pak, Uthmani, Simple, Tajweed, and clean vowelled scripts.
- **Word-by-Word Analysis**: Word-level breakdown with roots, morphology, and translations.
- **GitHub Friendly**: All individual files are kept under 75 MB, eliminating Git LFS bandwidth quotas and allowing direct consumption via `raw.githubusercontent.com`.

---

## 📂 Repository Structure

```
quran_text/
├── metadata/
│   ├── surah_list.json               # All 114 Surahs with metadata (revelation, verses, rukus)
│   ├── juz_index.json                # 30 Juz boundaries and ayah ranges
│   ├── manzil_index.json             # 7 Manzils
│   └── ruku_index.json               # Ruku classifications
├── quran_categories.json             # Master index of all 49 languages, editions, and file paths
├── quran_manifest.json               # Detailed file index and sizes
├── full_quran_arabic/                # Complete Quran across 6 authentic script styles
├── full_quran_translations/          # 106 full translations grouped into 49 language folders
│   ├── english/                      # Sahih International, Pickthall, Yusuf Ali, Arberry, etc.
│   ├── urdu/                         # Fateh Muhammad Jalandhari, Taqi Usmani, Maududi, etc.
│   ├── hindi/                        # Hindi translations
│   └── [46 other languages]/
├── full_quran_tafsir/                # 25 authoritative exegeses grouped by language
│   ├── arabic/                       # Tafsir Ibn Kathir, Al-Qurtubi, Al-Tabari, Al-Sa'di, etc.
│   ├── urdu/                         # Bayan-ul-Quran (Dr. Israr), Ibn Kathir, Maududi, etc.
│   ├── english/                      # Ma'arif-ul-Qur'an, Tafheem-ul-Qur'an, Ibn Kathir English
│   ├── hindi/                        # Maududi Hindi Commentary
│   ├── merge_tafsir.py               # Optional script to merge split parts locally
│   └── split_tafsir_manifest.json    # Part mapping for multi-part tafsir files
├── full_quran_word_by_word/          # Word-by-word translations (English, Urdu, Hindi, etc.)
└── surah_001/ ... surah_114/         # Individual Surah folders (Optimal for Mobile Apps)
    ├── complete.json                 # ⭐ Single unified file with all verses, translations & tafseers
    ├── arabic/                       # Arabic script variations for this Surah
    ├── translations/                 # Translations by language for this Surah
    ├── tafsir/                       # Tafseer commentaries by language for this Surah
    └── word_by_word/                 # Word-by-word breakdown for this Surah
```

---

## 🚀 How to Use in Your App

### 1. Fetching a Complete Surah (Recommended for Mobile)

Instead of making dozens of API calls, load a complete Surah with all its content in a single HTTP GET:

```dart
// Dart / Flutter Example
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<Map<String, dynamic>> loadSurah(int surahNumber) async {
  final padded = surahNumber.toString().padLeft(3, '0');
  final url = 'https://raw.githubusercontent.com/muqeetiqbal2/Quran-Text-with-Translations-And-Tafsirs/main/surah_$padded/complete.json';
  
  final response = await http.get(Uri.parse(url));
  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  } else {
    throw Exception('Failed to load Surah $surahNumber');
  }
}
```

### 2. Loading the Category & Edition Catalog

To display available languages and translations to the user:

```typescript
// TypeScript / React / Node.js
async function getCatalog() {
  const url = 'https://raw.githubusercontent.com/muqeetiqbal2/Quran-Text-with-Translations-And-Tafsirs/main/quran_categories.json';
  const res = await fetch(url);
  const catalog = await res.json();
  console.log(`Available Languages: ${catalog.translations_summary.total_languages}`);
  return catalog;
}
```

---

## 📚 Categorized Collections

### 🌐 Translations by Language (Sample)
- **Urdu**: Fateh Muhammad Jalandhari, Mufti Taqi Usmani, Syed Abul A'la Maududi, Ahmed Raza Khan, Dr. Tahir-ul-Qadri, Amin Ahsan Islahi.
- **English**: Sahih International, Abdullah Yusuf Ali, Marmaduke Pickthall, Arthur John Arberry, Muhammad Asad, Dr. Mustafa Khattab.
- **Other Languages**: Arabic, Bengali, Indonesian, Malay, Turkish, Persian, French, German, Spanish, Russian, Chinese, Hindi, Tamil, Telugu, Malayalam, Pashto, Sindhi, and 33 more.

### 📜 Tafsir (Commentary) Collections
- **Arabic**: *Tafsir Ibn Kathir*, *Tafsir al-Qurtubi*, *Tafsir al-Tabari*, *Tafsir al-Sa'di*, *Tafsir al-Baghawi*, *Tafsir al-Waseet (Tantawi)*, *Tafsir al-Muyassar*.
- **Urdu**: *Bayan-ul-Quran (Dr. Israr Ahmad)*, *Tafheem-ul-Quran (Maududi)*, *Tafsir Ibn Kathir (Urdu)*, *Ma'ariful Quran (Mufti Shafi)*, *Tadabbur-ul-Quran (Islahi)*, *Tibyan-ul-Quran*, *Fi Zilal al-Quran*.
- **English**: *Ma'ariful Quran (Mufti Shafi)*, *Tafheem-ul-Quran (Maududi)*, *Tafsir Ibn Kathir English*.
- **Hindi**: *Tafheem-ul-Quran Hindi*.

---

## 🛠️ Offline Usage & Recombining Multi-Part Tafsirs

All per-surah folders (`surah_001` to `surah_114`) contain complete, ready-to-use tafsirs. 

For offline bulk processing where you need the entire Quran commentary in a single JSON file, run:

```bash
cd full_quran_tafsir
python merge_tafsir.py
```

This will automatically merge any split parts into a single monolithic JSON file.

---

## ⚖️ License & Attribution

This dataset is compiled for educational, research, and non-commercial Islamic software development. All Quranic Arabic texts and canonical translations are verified against authenticated open-source corpora.

