#!/bin/sh
# export PATH="${PATH}:$HOME/.local/bin"
# ln -s $HOME/codding/tr.py $HOME/.local/bin/mytrans
TEXT=$(xclip -selection primary -o)
TRANS=$(mytrans ru-en "$TEXT")

if [ "$TRANS" ]; then
gxmessage -geometry 1000x800 -bg "#aaaaaa" -title "Translate" -wrap -center -fn  "Droid 24"  "$TRANS"
else
gxmessage -geometry 260x140 -bg "#aaaaaa" -title "Translate" -wrap -center -fn  "Droid 24" "Нет связи с сервисом"
fi