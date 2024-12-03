#!/bin/sh

grep -v STATS < README.md > README.md.tmp
wc -c golfs/* | xargs -n 2 sh -c 'echo \| \`$1\` \| \`$0\` \| "<!-- STATS -->"' >> README.md.tmp
mv README.md.tmp README.md
