#　仮想環境の構築
## ターミナルで構築
```
python3 -m venv foo_env
```
foo_envディレクトリが作られる \
ディレクリに移動(次のコマンドにパスを含めば移動しなくていい) \
仮想環境の実行
```
bin/ source activate
```
仮想環境の停止
```
deactivate
```
##　pipコマンドで実行
仮想環境の実行
```
pipenv shell
```
仮想環境の停止
```
exit
```