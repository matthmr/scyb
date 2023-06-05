#!/bin/sh

sed -n '/^UC/p' subscriptions.csv |\
  sed 's/,/	/2;s/,/	/;s/"//g' > subscriptions.tsv

SUBS=$(wc -l subscriptions.tsv | awk '{print $1}')

# index.js
echo "[ .. ] Generating \`index.js'"
awk -F'	' '
BEGIN {
  print("const yt_channels = [");
}
{
  printf("{id: \"%s\", name: \"%s\"},\n", $1, $3);
}
END {
  print("];");
}' subscriptions.tsv |\
  cat - index.js.in > index.js

# index.html
echo "[ .. ] Generating \`index.html'"
sed "s/@BUTTONS-COUNT@/${SUBS}/g" index.html.in > index.html
