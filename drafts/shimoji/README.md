# 『あなたのスマホは、なぜ乗っ取られるのか？』執筆管理

非エンジニア向けに、インターネットの仕組みからサイバー攻撃と日常の対策までを解説する、技術書典向け全20ページの原稿です。

このディレクトリの `p01.md`〜`p20.md` を承認済み原稿の正本とし、`images/` 内の対応画像を採用図として管理します。Markdown内の相対リンクにより、本文と図を続けてプレビューできます。画像の配置位置は編集上の仮位置であり、ページ番号は印刷組版後のページ番号とは限りません。

## 構成・レビュー状況

### はじめに（P1〜P2）

| ページ | 内容 | 原稿 | 採用図 | 状況 |
| --- | --- | --- | --- | --- |
| P1 | インターネットとWeb、ブラウザは何が違う？ | [p01.md](p01.md) | [figure01.png](images/figure01.png) | 本文・図 承認済み |
| P2 | Webサイトとアプリは何が違う？ | [p02.md](p02.md) | [figure02.png](images/figure02.png) | 本文・図 承認済み |

### 第1章　インターネットの仕組み（P3〜P8）

| ページ | 内容 | 原稿 | 採用図 | 状況 |
| --- | --- | --- | --- | --- |
| P3 | 検索ボタンを押すと、何が起こる？ | [p03.md](p03.md) | [figure03.png](images/figure03.png) | 本文・図 承認済み |
| P4 | スマホは、どうやって目的のサーバーを見つける？ | [p04.md](p04.md) | [figure04.png](images/figure04.png) | 本文・図 承認済み |
| P5 | インターネットの情報は、どうやって届く？ | [p05.md](p05.md) | [figure05.png](images/figure05.png)、補足図 [figure05_tcp.png](images/figure05_tcp.png) | 本文・図 承認済み |
| P6 | Webサイトの画面は、どうやって作られる？ | [p06.md](p06.md) | [figure06.png](images/figure06.png) | 本文・図 承認済み |
| P7 | HTTPSは、どうやって通信を守っている？ | [p07.md](p07.md) | [figure07.png](images/figure07.png) | 本文・図 承認済み |
| P8 | インターネットには、どんな危険が潜んでいる？ | [p08.md](p08.md) | [figure08.png](images/figure08.png) | 本文・図 承認済み |

### 第2章　ハッキングの仕組み（P9〜P16）

| ページ | 内容 | 原稿 | 採用図 | 状況 |
| --- | --- | --- | --- | --- |
| P9 | ハッキングとは何か？ | [p09.md](p09.md) | [figure09.png](images/figure09.png) | 本文・図 承認済み |
| P10 | 攻撃者は、どうやって狙う相手を見つける？ | [p10.md](p10.md) | [figure10.png](images/figure10.png) | 本文・図 承認済み |
| P11 | パスワードは、どうやって盗まれる？ | [p11.md](p11.md) | [figure11.png](images/figure11.png) | 本文・図 承認済み |
| P12 | Webサイトの弱点は、どうやって悪用される？ | [p12.md](p12.md) | [figure12.png](images/figure12.png) | 本文・図 承認済み |
| P13 | サーバーに侵入されると、何が起こる？ | [p13.md](p13.md) | [figure13.png](images/figure13.png) | 本文・図 承認済み |
| P14 | ウイルスやランサムウェアは何をする？ | [p14.md](p14.md) | [figure14.png](images/figure14.png) | 本文・図 承認済み |
| P15 | 社会を止めるサイバー攻撃とは？ | [p15.md](p15.md) | [figure15.png](images/figure15.png) | 本文・図 承認済み |
| P16 | なぜ、サイバー攻撃を完全には防げない？ | [p16.md](p16.md) | [figure16.png](images/figure16.png) | 本文・図 承認済み |

### 第3章　セキュリティ対策（P17〜P20）

| ページ | 内容 | 原稿 | 採用図 | 状況 |
| --- | --- | --- | --- | --- |
| P17 | パスワードとログインを守るには？ | [p17.md](p17.md) | [figure17.png](images/figure17.png) | 本文・図 承認済み |
| P18 | スマホやアプリを安全に使うには？ | [p18.md](p18.md) | [figure18.png](images/figure18.png) | 本文・図 承認済み |
| P19 | 怪しいメールや偽サイトを見抜くには？ | [p19.md](p19.md) | [figure19.png](images/figure19.png) | 本文・図 承認済み |
| P20 | 今日から始めるセキュリティ対策 | [p20.md](p20.md) | [figure20.png](images/figure20.png) | 本文・図 承認済み |

## ファイル構成

- `p01.md`〜`p20.md`：ページ別の承認済み原稿
- `images/figure01.png`〜`images/figure20.png`：各ページの採用図
- `images/figure05_tcp.png`：P5のTCP補足図
- `README.md`：構成・レビュー状況・統合手順
- `WRITING_GUIDELINES.md`：執筆・レビュー・デザインのガイドライン

## 原稿と画像の管理ルール

- 承認済みの原稿本文、採用画像、ページ構成を変更する場合は、対象と変更理由を明確にして再レビューする。
- 本文中の画像参照は、実際の保存ファイル名と一致させる。
- 確定したMarkdownファイルを正本とし、会話の記憶から過去の文章を再構築しない。
- `articles/shimoji.re` は統合作業を開始するまで変更しない。
- GitHubへのpush、Pull Request作成、リモートブランチの変更は、執筆者の明示的な承認を得てから行う。

## Re:VIEWへの統合時の確認事項

1. P1〜P20の本文と全21画像が揃い、すべて承認済みであることを確認する。
2. Markdown内の画像参照と実ファイルが一致することを確認する。
3. `articles/shimoji.re` との差分とRe:VIEW記法への変換内容を確認する。
4. 統合後にローカルでビルドと校正を実行する。

