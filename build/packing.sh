#!/bin/zsh

# .app ファイルを生成する

# .shファイルのあるディレクトリに移動
cd `dirname $0`

# define vars
# icon=""
name="DB3 Character Maker"
# echo -n ver=
# read ver
ver="0.01"
copy="(c) fifth_day"
bundleId="fifth_day.db3-character-maker"

# flet run
flet pack ../scripts/character_maker.py --name "$name" --product-name "$name" --product-version $ver --copyright "$copy" --bundle-id "$bundleId"

echo "finish"
