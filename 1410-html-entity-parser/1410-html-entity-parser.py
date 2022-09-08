class Solution(object):
    def entityParser(self, text):
        d = {
             '&quot;': '"',
             '&apos;': "'",
             '&amp;': '&',
             '&gt;': '>',
             '&lt;': '<',
             '&frasl;': '/'
            }
        rePattern = re.compile("(" + "|".join(d.keys()) + ")")
        return rePattern.sub(lambda x:d[x.group(0)], text)
                