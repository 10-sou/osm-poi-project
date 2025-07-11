# osm-poi-project

Vue.js + Laravel 製の Web アプリケーションで、OpenStreetMap (OSM) から抽出した POI（病院・コンビニなど）を対象区ごとに検索・地図表示できます。

## 🔍 概要

本プロジェクトは、指定したエリア（高津区・宮前区）内の POI を、メッシュ単位で検索・可視化するツールです。  
行政区、カテゴリ（病院・コンビニなど）、タグ（施設名）を選択することで、対応する POI 情報が地図と一覧に表示されます。

- バックエンド：Laravel (API)
- フロントエンド：Vue 3 (Vite)
- データベース：MySQL
- 地図表示：Leaflet.js

Qiitaでの解説記事はこちら →  
🔗https://qiita.com/firstnose0306/items/7c3adb0a8546193a792e


---

## ✨ 主な機能

- 高津区・宮前区の POI をカテゴリ・タグ別に絞り込み
- OSMから取得したメッシュ単位の位置情報を表示
- Vue + Laravel によるシンプルなSPA構成
- POIタグやエリアの拡張が容易

---

## 🚀 デモ（スクリーンショット）
![Animation 2](https://github.com/user-attachments/assets/d676879d-1e98-4cce-817d-77bb29418692)

---

## 📦 セットアップ手順

### 1. リポジトリをクローン

```bash
git clone https://github.com/10-sou/osm-poi-project.git
cd osm-poi-project
```

### 2. バックエンド（Laravel）

```bash
cd backend
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate --seed
php artisan serve
```

### 3. フロントエンド（Vue）

```bash
cd ../frontend
npm install
npm run dev
```

---

## 🗺️ 使い方

1. 区（高津区 or 宮前区）を選択
2. カテゴリ（病院 / コンビニ）を選択
3. タグ（施設名）を選択
4. 「検索」ボタンを押すと、該当する POI のメッシュIDと位置情報が表示され、地図にプロットされます

---

## 🧩 データ構造とAPI

### テーブル例

| テーブル名       | 内容                   |
|------------------|------------------------|
| `takatu_mesh`    | 高津区のPOIメッシュデータ |
| `miyamae_mesh`   | 宮前区のPOIメッシュデータ |

### APIエンドポイント

| エンドポイント             | 内容                           |
|----------------------------|--------------------------------|
| `GET /api/tag-options`     | 区＋カテゴリに応じたタグ一覧       |
| `GET /api/search`          | 区＋タグに応じた検索結果（位置情報） |

---

## 📂 ディレクトリ構成

```bash
osm-poi-project/
├── backend/        # Laravelアプリ
├── frontend/       # Vue 3 + Vite アプリ
└── README.md
```

---

## 🔧 拡張方法

- 対象エリアの追加：SeederファイルとDBテーブルを用意し、Controllerにマッピングを追記
- カテゴリやタグの追加：`MeshTagController` 内の辞書に追記するだけで対応可能

---

## 🧭 使用データとライセンスについて

本プロジェクトで使用している POI データは、OpenStreetMap から抽出されたものです。  
**OpenStreetMap のデータは [Open Database License (ODbL)](https://www.openstreetmap.org/copyright) に基づいて提供されています。**

本プロジェクトを利用・再配布する際は、以下にご注意ください：

- データ元が OpenStreetMap であることを明記すること
- データを改変した場合、その旨を明示すること
- データ自体は ODbL ライセンスに従って扱う必要があります

📌 詳細はこちら：https://www.openstreetmap.org/copyright

---

## 📝 ライセンス

このプロジェクトのコードは MIT ライセンスで提供されています。  
データのライセンス（ODbL）とは異なるため、再利用時には両者にご注意ください。

---

## 🙋 作者・貢献

作成者：[10-sou](https://github.com/10-sou)

Pull Request / Issue / 改善提案など大歓迎です！
