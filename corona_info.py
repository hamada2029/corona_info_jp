from requests import Session
import re
from pathlib import Path
import time


LINK_P = re.compile('<link [^>]+>')
SCRIPT_P = re.compile('<script [^>]+></script>')
SCRIPT_W = 'o=t.hideFacility;'
SCRIPT_W2 = 'location.replace("https://newsdigest.jp/pages/coronavirus/?ref=illegal_mirror")'
SCRIPT_W3 = 'location.replace("https://newsdigest.jp/pages/coronavirus/?ref=pc")'
ADD_SCRIPT = 'console.log(a);localStorage.setItem("a", JSON.stringify(a, null, 4));'
DR = Path(__file__).parent


class CoronaInfo:
    def __init__(self):
        self.ses = Session()
        self.ses.cookies['ref'] = 'nd_app'
        self.url = 'https://newsdigest.jp/pages/coronavirus/'
        self.myscript_dr = DR / 'myscript'
        self.myscript_dr.mkdir(exist_ok=True)
        for sfp in self.myscript_dr.iterdir():
            sfp.unlink()
        self.cur_p = DR / 'cur.html'

    def get(self):
        r = self.ses.get(self.url)
        self.s = r.text
        self.links = LINK_P.findall(self.s)
        self.scripts = SCRIPT_P.findall(self.s)

    def replace_slug_script(self):
        for link in self.links:
            if '%5B...slug%5D.js' in link:
                link_url = link.split('href="')[1].split('"')[0]
                link_fn = '[...slug].js'
                r = self.ses.get(link_url)
                link_s = r.text
                link_s = link_s.replace(SCRIPT_W2, 'function(){}')
                link_s = link_s.replace(SCRIPT_W3, 'function(){}')
                fp = self.myscript_dr / link_fn
                fp.write_text(link_s)
                self.s = self.s.replace(link, '')
                break
        else:
            raise ValueError('links')

        for script in self.scripts:
            if '%5B...slug%5D.js' in script:
                self.s = self.s.replace(
                    script,
                    '<script src="myscript/%5B...slug%5D.js?{}"></script>'.format(time.time())
                )
                break

        # self.s = self.s.replace('"/pages/[...slug]"', 'null')
        self.cur_p.write_text(self.s)

    def replace_data_script(self):
        for link in self.links:
            if '/_next/static/chunks/' not in link:
                continue
            link_url = link.split('href="')[1].split('"')[0]
            link_fn = link_url.split('/')[-1]
            r = self.ses.get(link_url)
            link_s = r.text
            if SCRIPT_W in link_s:
                link_s = link_s.replace(SCRIPT_W, SCRIPT_W + ADD_SCRIPT)
                fp = self.myscript_dr / link_fn
                fp.write_text(link_s)
                self.s = self.s.replace(link, '')
                print(link_fn)
                break
        else:
            raise ValueError('links')

        for script in self.scripts:
            if link_fn in script:
                self.s = self.s.replace(
                    script,
                    '<script src="myscript/{}?{}"></script>'.format(link_fn, time.time())
                )
                break

        self.s = self.s.replace(
            'sendAdserverRequest();',
            """
            sendAdserverRequest();
            document.querySelector('h1').innerHTML = document.querySelector('h1').innerHTML + '<br><a href="table.html" target="_blank">クリックで一覧表示</a>';
            """
        )
        self.cur_p.write_text(self.s)


def main():
    """Main."""
    ci = CoronaInfo()
    ci.get()
    ci.replace_slug_script()
    ci.replace_data_script()
    print('cur.htmlをブラウザで開いてください。')


if __name__ == '__main__':
    main()
