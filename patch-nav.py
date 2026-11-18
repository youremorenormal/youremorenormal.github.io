"""Adds 'For reviewers and podcast hosts' to the header 'Browse the shelves' menu on every page. Idempotent."""
import glob
OLD = '<a href="https://youremorenormal.com/about/">About the author</a></div></div></details>'
NEW = '<a href="https://youremorenormal.com/about/">About the author</a><a href="https://youremorenormal.com/press/">For reviewers and podcast hosts</a></div></div></details>'
n = 0
for p in glob.glob("**/index.html", recursive=True):
    s = open(p, encoding="utf8").read()
    if OLD in s and "press/\">For reviewers and podcast hosts</a></div></div></details>" not in s:
        open(p, "w", encoding="utf8").write(s.replace(OLD, NEW)); n += 1
print("nav", n)
