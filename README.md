# corona_info_jp
  
新型コロナウイルス 日本国内の感染状況 PC用ミラーサイト
newsdigestより1時間毎に取得  
スマートフォンが無くてもブラウザから施設名、住所などが確認できます。  
  
  
[https://script.google.com/macros/s/AKfycbydQstaIcF5rcuAUBZRemtPOSyEyREqTCjqCijWWntcx5IL4Cw/exec](https://script.google.com/macros/s/AKfycbydQstaIcF5rcuAUBZRemtPOSyEyREqTCjqCijWWntcx5IL4Cw/exec)  
  
  

### curlで最新状態をダウンロードする方法
```
curl -H 'Cookie: ref=nd_app' 'https://newsdigest.jp/pages/coronavirus/' > cur.html
```  
実行後にブラウザでcur.htmlファイルを開くと見れます。  


