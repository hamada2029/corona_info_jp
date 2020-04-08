from pathlib import Path
from requests import Session
import re


DR = Path(__file__).parent
P1 = re.compile('<link rel="preload" href="https://app-static.newsdigest.jp/corona/_next/static/chunks/e7c464a8[^"]+" as="script"/>')
P2 = re.compile('<script src="(https://app-static.newsdigest.jp/corona/_next/static/chunks/e7c464a8[^"]+)" async="">')

DLCODE = """
let exflag = false;

function _dl(n){
    if(exflag){return;}
    let csv_s = '"prefecture","name","reports","disinfected","address","firstRelease","lastEdited"\n';
    for(let i=0; i<n.length; i++){
        let e = n[i];
        csv_s += '"' + e.prefecture + '","' + e.name + '","' + e.reports + '","' + e.disinfected + '","' + e.address + '","' + e.firstRelease + '","' + e.lastEdited + '"\n'
    }

    let a = document.createElement("a");
    a.href = URL.createObjectURL(
        new Blob([csv_s], {type: "text/csv"})
    );
    let t = new Date().getTime();
    a.setAttribute("download", 'data' + t + '.csv');
    a.click();
    exflag = true;
}

"""


def main():
    """Main."""
    ses = Session()
    url = 'https://newsdigest.jp/pages/coronavirus/'
    ses.cookies['ref'] = 'nd_app'
    r = ses.get(url)
    s = r.text

    js_url = P2.search(s).groups()[0]
    print(js_url)
    r = ses.get(js_url)
    js = r.text
    js = DLCODE + js
    js = js.replace(
        'o.useEffect((function(){',
        '_dl(n);o.useEffect((function(){'
    )
    jp = DR / 'e7c464a8.js'
    jp.write_text(js)

    s = P1.sub('', s)
    s = P2.sub('<script src="e7c464a8.js">', s)
    fp = DR / 'tmp.html'
    fp.write_text(s)

    print('tmp.htmlをブラウザで開くと住所データが自動でダウンロードされます。')


if __name__ == '__main__':
    main()
