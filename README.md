# AtCoder

2026-04-25: AtCoder を始めた. 
今の目標はとりあえず茶色. 

## AtCoder CLI

Atcoder CLI では`atcoder-cli` (`acc`) と `online-judge-tools` (`oj`) を使う. 

導入手順の記録:
```bash
npm install -g atcoder-cli
uv tool install --force --python 3.11 online-judge-tools
```

(`online-judge-tools` は Python 3.12 だと `distutils` がなくて失敗したため, Python 3.11 を指定して入れた. )

## 基本操作

新しいコンテストを始める:
```bash
acc new abc413
```

問題選択画面で問題を選ぶ:
- `Space`: 選択 / 解除
- `a`: 全選択 / 全解除
- `i`: 選択を反転
- `Enter`: 決定

**既に作ったコンテストにあとから問題を追加する:**
```bash
cd abc413
acc add
```

**未作成の問題を全部追加する:**

```bash
acc add -c rest
```

**すべての問題を対象にする:**
```bash
acc add -c all
```

**テストする:**
```bash
oj test -c "python3 main.py"
```

提出:
```bash
acc submit main.py
```

`acc submit` は現在いるディレクトリと `contest.acc.json` から提出先の問題を判断する.

## 個人的に作ったエイリアス
`main.py` というファイル名やテストケースの相対パスは基本固定なので, `ojt` でテストケースを検証できるようにした. 
`~/.zshrc` に下記を追加すれば OK. 

```bash
ojt() {
    oj test -d tests -c "${*:-python3 main.py}"
}
```
- `-d`: テストケースのディレクトリ
- `-c`: 実行ファイル
