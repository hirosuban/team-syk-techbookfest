# プロジェクト概要

技術書典の合同誌の**原稿リポジトリ**。Re:VIEW でビルドする書籍本体をここで管理する。
執筆は著者3人（yamane / shimoji / kai）で分担し、各自の章は `articles/<name>.re`。

- `articles/catalog.yml` … 章立て（PREDEF / CHAPS / APPENDIX / POSTDEF）
- `articles/*.re` … 各著者の原稿（Re:VIEW 形式）
- `articles/doc/` … Re:VIEW 本体の記法リファレンス（`format.ja.md` ほか）

## yamane 章（デミオ／OBD運転採点）の執筆ルール

yamane が担当するのは「ペーパードライバー、OBDに運転を採点される」章（`articles/yamane.re`）。
この章は**別リポジトリ `techbookfest21`** の研究プロジェクトを素材にしている。

### 素材リポジトリの場所

隣接する `../techbookfest21`（`/Users/my/Documents/workspace/techbookfest21`）。主な参照先:

- `docs/chapter_outline.md` … **章の骨子（章立て・ページ配分）。この章の構成の正本。**
  パス・ファイル名は固定（向こうの CLAUDE.md で移動・改名・削除禁止と明記）。
- `docs/obd2_csv.md` … OBD2の機材・接続手順・取得項目・記録前チェックリスト。
- `scripts/obd/*.py` … 図表を出す研究スクリプト（load_obd_log / gap_utils / plot_speed_over_time /
  plot_multi_metric / score_driving / mpl_ja）。
- `obd_log/*.csv` … 実走行ログ（10/4・10/12・10/17×2・10/18）。
- `logs/YYYY-MM-DD.md` … 研究ログ（相関0.98などの根拠はここ）。

### Claude の役割分担（重要）

- **本文は著者(yamane)が手で書くのを優先する。** Claude が勝手に本文を書き替えると、
  著者の手書き分と衝突する前提で動くこと。地の文を大量生成して上書きしない。
- Claude の担当は (1) 骨子→Re:VIEW の**器（見出し構造）の整備**、
  (2) **事実確認**（行数・列数・閾値・項目名などを実データ/スクリプトで裏取り）、
  (3) 図表を出すスクリプトの実行補助。
- 数値・固有名詞は記憶で書かず、必ず `../techbookfest21` の実データ・スクリプト・ログで裏取りする。
- 既に本文が書かれている節を編集するときは、消す前に内容を確認し、著者の意図と食い違うなら
  勝手に消さず指摘する。

### Re:VIEW の約束ごと

- 見出し: `=` 章 / `==` 節 / `===` 項 / `====` 目（節番号は Re:VIEW が自動採番するので手書きしない）。
- 執筆メモ・TODO・参照は `#@#` 行で書く（最終出力に出ないコメント）。本文はメモの下に地の文で書き、
  書き終えたメモは消す。
- 図は `//image`、表は `//table`、リストは `//list` など（`articles/doc/format.ja.md` 参照）。
