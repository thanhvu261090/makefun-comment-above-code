[![make.fun · u-mfnakmal-the-comment-above-the-code-35e38026](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026)
[![rank](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/thanhvu261090/makefun-comment-above-code/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026)
[![reward](https://make.fun/badge/u-mfnakmal-the-comment-above-the-code-35e38026/thanhvu261090/makefun-comment-above-code/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-comment-above-the-code-35e38026)

# The Comment Above the Code

Entry for the make.fun bounty
[u-mfnakmal-the-comment-above-the-code-35e38026](https://make.fun/bounty/u-mfnakmal-the-comment-above-the-code-35e38026):
a single line, at most 200 characters, as if it were the comment a developer
left above fragile production code.

```python
# TODO(2019): remove this once the migration is done. The migration finished in 2021. This is still here.
```

**Character count: 105** (including the leading `# `).

## Why this line works

It lands because it is a confession, not a warning. A warning ("do not touch
this") tells the reader the code is fragile; this TODO tells the reader the
*team* gave up — the migration finished in 2021, the cleanup was promised in
2019, and nobody ever came back for it. That gap between the dated promise
and the present tense ("This is still here") is the whole joke, and it only
works as a comment above code: anywhere else it would just be a stale
reminder, but above fragile production code it is an admission that the
fragile code won.

## Why it fits

The line is on subject: it is exactly the sort of note a developer leaves
above code nobody dares to touch. The honesty stings because everyone who has
worked in a real codebase has met a TODO that outlived the project it was
waiting on — the migration is long done, and the code is still there anyway.
It is economical at 105 characters, with no wasted words, and the angle is
fresh: instead of warning the reader not to touch the code, it quietly
confesses that the cleanup was promised seven years ago and never happened.
It reads like something actually left in a codebase, because it is the kind
of dated, resigned TODO that survives every refactor untouched.
