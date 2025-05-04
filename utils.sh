#!/bin/bash
for i in {1..8}; do
  for n in {1..20}; do
    dir="dataset/problem_$i"
    original="$dir/answer_${n}.md"
    revised="$dir/answer_${n}_revised.md"
    if [ -f "$revised" ]; then
      [ -f "$original" ] && rm "$original"
      mv "$revised" "$original"
    fi
  done
done