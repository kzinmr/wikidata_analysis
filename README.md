# Extract (key-entity, property, value-entity) triples from Wikidata

## Get JSON dumps (`latest-all.json.gz`)
See. https://www.wikidata.org/wiki/Wikidata:Database_download/

```
 $ wget https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.gz
 ```

 Final Access: 26-Nov-2019

## About Wikidata

See. https://www.mediawiki.org/wiki/Wikibase/DataModel/JSON

### Labels, Descriptions and Aliases
- `"labels"`, `"descriptions"`, `"aliases"` have language code keys like `"en"`, `"ja"`

### Statements
- the **Statement** is about the **Property**
   - there can be multiple Statements about the same Property in a single Entity
- `"claims"` has property code keys like `"P17"`
- A **Snak** provides some kind of information about a specific Property of a given Entity.

```
{
  "claims": {
    "P17": [
      {
        "id": "q60$5083E43C-228B-4E3E-B82A-4CB20A22A3FB",  # statement id
        "mainsnak": {
          "snaktype": "value",
          "property": "P17",   # same as the key property code
          "datatype": "wikibase-item",  # See. Datatypes
          "datavalue": {  # If the snaktype is "value"
            "value": {  # Example of wikibase-entityid
              "entity-type": "item",   #  item or property
              "id": "Q30",
              "numeric-id": 30
            },
            "type": "wikibase-entityid"  # See. Datatypes (value type)
          }
        },
        "type": "statement",
        "rank": "normal",
        "qualifiers": {
          "P580": [],
          "P5436": []
         }
        "references": [
           {
             "hash": "d103e3541cc531fa54adcaffebde6bef28d87d32",
             "snaks": []
           }
         ]
      }
    ]
  }
}
```

#### Datatypes
See. https://www.wikidata.org/wiki/Special:ListDatatypes

- Item (Wikibase entity id)
   - Link to other Items on the project.
   - The value type for this data type is `wikibase-entityid`.

- Property (Wikibase entity id)
   - Link to Properties on the project. 
   - The value type for this data type is `wikibase-entityid`.

### Properties
Property code definitions can be obtained by following:

cf. [List of All Properties](https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all)

#### Install wikibase-cli to fetch the list of properties
```
$ sudo docker run -it --rm -t maxlath/wikibase-cli
$ alias wb="sudo docker run --rm -t maxlath/wikibase-cli"
$ wb props --lang ja --details -e https://query.wikidata.org/sparql > props_ja.json
```

## Preprocess `latest-all.json.gz`
超マルチコアCPU環境で実行すれば数時間内に完了
実行例.
```
python split.py
ls /workspace/wikidata/split/latest-split-*.json.gz|parallel -j 18 "python process_wikidata.py {}"
```

## Extract Triples

See. `wikidata-preprocess.ipynb`

## Contents Analysis

See. `wikidata-view.ipynb`

- 元データから加工された入力データ(*.jsonl)の1行例(`ベルギー` ページに対応)
```
{"title_ja": "ベルギー", "id": "Q31", "properties": [{"id": "P5658", "property_midasi": {"ja": "railway traffic side", "en": "railway traffic side", "type": "WikibaseItem"}, "entities": [{"id": "Q13196750", "entity_midasi": "左"}]}, {"id": "P2852", "property_midasi": {"ja": "緊急電話番号", "en": "emergency phone number", "type": "WikibaseItem"}, "entities": [{"id": "Q1061257", "entity_midasi": "112番"}, {"id": "Q25648793", "entity_midasi": "100番"}, {"id": "Q25648794", "entity_midasi": "101番"}]}, {"id": "P36", "property_midasi": {"ja": "行政中心地", "en": "capital", "type": "WikibaseItem"}, "entities": [{"id": "Q239", "entity_midasi": "ブリュッセル＝ヴィル"}]}, {"id": "P2633", "property_midasi": {"ja": "主題の地理", "en": "geography of topic", "type": "WikibaseItem"}, "entities": [{"id": "Q1115035", "entity_midasi": "ベルギーの地理"}]}, {"id": "P2853", "property_midasi": {"ja": "コンセントの種類", "en": "electrical plug type", "type": "WikibaseItem"}, "entities": [{"id": "Q1378312", "entity_midasi": "ユーロプラグ"}]}, {"id": "P1792", "property_midasi": {"ja": "当地の人々のカテゴリ", "en": "category of associated people", "type": "WikibaseItem"}, "entities": [{"id": "Q7021332", "entity_midasi": "Category:ベルギーの人物"}]}, {"id": "P1343", "property_midasi": {"ja": "掲載している事典", "en": "described by source", "type": "WikibaseItem"}, "entities": [{"id": "Q302556", "entity_midasi": "カトリック百科事典"}, {"id": "Q2657718", "entity_midasi": "アルメニア・ソビエト百科事典"}, {"id": "Q4114391", "entity_midasi": "シティン軍事百科事典"}, {"id": "Q602358", "entity_midasi": "ブロックハウス・エフロン百科事典"}]}, {"id": "P122", "property_midasi": {"ja": "政治体制", "en": "basic form of government", "type": "WikibaseItem"}, "entities": [{"id": "Q41614", "entity_midasi": "立憲君主制"}]}, {"id": "P237", "property_midasi": {"ja": "紋章", "en": "coat of arms", "type": "WikibaseItem"}, "entities": [{"id": "Q199614", "entity_midasi": "ベルギーの国章"}]}, {"id": "P421", "property_midasi": {"ja": "標準時間帯", "en": "located in time zone", "type": "WikibaseItem"}, "entities": [{"id": "Q25989", "entity_midasi": "中央ヨーロッパ時間"}, {"id": "Q6655", "entity_midasi": "UTC+1"}, {"id": "Q6723", "entity_midasi": "UTC+2"}, {"id": "Q207020", "entity_midasi": "中央ヨーロッパ夏時間"}]}, {"id": "P208", "property_midasi": {"ja": "行政府", "en": "executive body", "type": "WikibaseItem"}, "entities": [{"id": "Q390947", "entity_midasi": "連邦政府"}]}, {"id": "P361", "property_midasi": {"ja": "以下の一部分", "en": "part of", "type": "WikibaseItem"}, "entities": [{"id": "Q215669", "entity_midasi": "連合国"}]}, {"id": "P6", "property_midasi": {"ja": "行政府の長", "en": "head of government", "type": "WikibaseItem"}, "entities": [{"id": "Q950958", "entity_midasi": "シャルル・ミシェル"}]}, {"id": "P31", "property_midasi": {"ja": "分類", "en": "instance of", "type": "WikibaseItem"}, "entities": [{"id": "Q3624078", "entity_midasi": "主権国家"}, {"id": "Q43702", "entity_midasi": "連邦"}, {"id": "Q6256", "entity_midasi": "国"}]}, {"id": "P530", "property_midasi": {"ja": "国交のある国", "en": "diplomatic relation", "type": "WikibaseItem"}, "entities": [{"id": "Q32", "entity_midasi": "ルクセンブルク"}, {"id": "Q38", "entity_midasi": "イタリア"}, {"id": "Q183", "entity_midasi": "ドイツ"}, {"id": "Q347", "entity_midasi": "リヒテンシュタイン"}, {"id": "Q408", "entity_midasi": "オーストラリア"}, {"id": "Q212", "entity_midasi": "ウクライナ"}, {"id": "Q1246", "entity_midasi": "コソボ共和国"}, {"id": "Q142", "entity_midasi": "フランス"}, {"id": "Q145", "entity_midasi": "イギリス"}, {"id": "Q16", "entity_midasi": "カナダ"}, {"id": "Q252", "entity_midasi": "インドネシア"}, {"id": "Q35", "entity_midasi": "デンマーク"}, {"id": "Q43", "entity_midasi": "トルコ"}, {"id": "Q55", "entity_midasi": "オランダ"}, {"id": "Q77", "entity_midasi": "ウルグアイ"}, {"id": "Q833", "entity_midasi": "マレーシア"}, {"id": "Q843", "entity_midasi": "パキスタン"}, {"id": "Q865", "entity_midasi": "中華民国"}, {"id": "Q96", "entity_midasi": "メキシコ"}, {"id": "Q974", "entity_midasi": "コンゴ民主共和国"}, {"id": "Q30", "entity_midasi": "アメリカ合衆国"}, {"id": "Q159", "entity_midasi": "ロシア"}, {"id": "Q668", "entity_midasi": "インド"}, {"id": "Q41", "entity_midasi": "ギリシャ"}, {"id": "Q148", "entity_midasi": "中華人民共和国"}, {"id": "Q230", "entity_midasi": "ジョージア"}, {"id": "Q801", "entity_midasi": "イスラエル"}, {"id": "Q29999", "entity_midasi": "オランダ王国"}, {"id": "Q28", "entity_midasi": "ハンガリー"}]}, {"id": "P1464", "property_midasi": {"ja": "当地生まれの人のカテゴリ", "en": "category for people born here", "type": "WikibaseItem"}, "entities": [{"id": "Q7463296", "entity_midasi": "Category:ベルギー出身の人物"}]}, {"id": "P47", "property_midasi": {"ja": "隣の国または行政区画", "en": "shares border with", "type": "WikibaseItem"}, "entities": [{"id": "Q183", "entity_midasi": "ドイツ"}, {"id": "Q32", "entity_midasi": "ルクセンブルク"}, {"id": "Q142", "entity_midasi": "フランス"}, {"id": "Q55", "entity_midasi": "オランダ"}, {"id": "Q29999", "entity_midasi": "オランダ王国"}]}, {"id": "P417", "property_midasi": {"ja": "守護聖人", "en": "patron saint", "type": "WikibaseItem"}, "entities": [{"id": "Q128267", "entity_midasi": "ナザレのヨセフ"}]}, {"id": "P1622", "property_midasi": {"ja": "交通方法", "en": "driving side", "type": "WikibaseItem"}, "entities": [{"id": "Q14565199", "entity_midasi": "右"}]}, {"id": "P2184", "property_midasi": {"ja": "主題の歴史", "en": "history of topic", "type": "WikibaseItem"}, "entities": [{"id": "Q205317", "entity_midasi": "ベルギーの歴史"}]}, {"id": "P35", "property_midasi": {"ja": "元首", "en": "head of state", "type": "WikibaseItem"}, "entities": [{"id": "Q155004", "entity_midasi": "フィリップ・ド・ベルジック"}, {"id": "Q12971", "entity_midasi": "レオポルド1世"}, {"id": "Q12967", "entity_midasi": "レオポルド2世"}, {"id": "Q55008046", "entity_midasi": "アルベール1世"}, {"id": "Q12973", "entity_midasi": "レオポルド3世"}, {"id": "Q12976", "entity_midasi": "ボードゥアン1世"}, {"id": "Q3911", "entity_midasi": "アルベール2世"}, {"id": "Q445553", "entity_midasi": "シャルル・ド・ベルジック"}, {"id": "Q1079522", "entity_midasi": "エラスム＝ルイ・シュルレ・ド・ショキエ"}]}, {"id": "P78", "property_midasi": {"ja": "トップレベルドメイン", "en": "top-level Internet domain", "type": "WikibaseItem"}, "entities": [{"id": "Q39773", "entity_midasi": ".be"}]}, {"id": "P1344", "property_midasi": {"ja": "参加イベント", "en": "participant of", "type": "WikibaseItem"}, "entities": [{"id": "Q1088364", "entity_midasi": "アーズブルックの戦い"}]}, {"id": "P1313", "property_midasi": {"ja": "政府の長の職", "en": "office held by head of government", "type": "WikibaseItem"}, "entities": [{"id": "Q213107", "entity_midasi": "ベルギーの首相"}]}, {"id": "P163", "property_midasi": {"ja": "旗", "en": "flag", "type": "WikibaseItem"}, "entities": [{"id": "Q12990", "entity_midasi": "ベルギーの国旗"}]}, {"id": "P1830", "property_midasi": {"ja": "所有物", "en": "owner of", "type": "WikibaseItem"}, "entities": [{"id": "Q594406", "entity_midasi": "叛逆天使の墜落"}, {"id": "Q3052500", "entity_midasi": "ベルギー国立植物園"}]}, {"id": "P138", "property_midasi": {"ja": "名前の由来", "en": "named after", "type": "WikibaseItem"}, "entities": [{"id": "Q206443", "entity_midasi": "ガリア・ベルギカ"}]}, {"id": "P1304", "property_midasi": {"ja": "中央銀行", "en": "central bank", "type": "WikibaseItem"}, "entities": [{"id": "Q685918", "entity_midasi": "ベルギー国立銀行"}]}, {"id": "P910", "property_midasi": {"ja": "記事の中心カテゴリ", "en": "topic's main category", "type": "WikibaseItem"}, "entities": [{"id": "Q4366768", "entity_midasi": "Category:ベルギー"}]}, {"id": "P37", "property_midasi": {"ja": "公用語", "en": "official language", "type": "WikibaseItem"}, "entities": [{"id": "Q7411", "entity_midasi": "オランダ語"}, {"id": "Q150", "entity_midasi": "フランス語"}, {"id": "Q188", "entity_midasi": "ドイツ語"}]}, {"id": "P150", "property_midasi": {"ja": "直下の行政区画", "en": "contains administrative territorial entity", "type": "WikibaseItem"}, "entities": [{"id": "Q9337", "entity_midasi": "フランデレン地域"}, {"id": "Q240", "entity_midasi": "ブリュッセル首都圏地域"}, {"id": "Q89959", "entity_midasi": "フランス語共同体"}, {"id": "Q90027", "entity_midasi": "ドイツ語共同体"}, {"id": "Q231", "entity_midasi": "ワロン地域"}]}, {"id": "P209", "property_midasi": {"ja": "最高司法府", "en": "highest judicial authority", "type": "WikibaseItem"}, "entities": [{"id": "Q1755321", "entity_midasi": "ベルギー憲法裁判所"}]}, {"id": "P527", "property_midasi": {"ja": "以下を含む", "en": "has part", "type": "WikibaseItem"}, "entities": [{"id": "Q234", "entity_midasi": "フランドル"}]}, {"id": "P85", "property_midasi": {"ja": "アンセム", "en": "anthem", "type": "WikibaseItem"}, "entities": [{"id": "Q161539", "entity_midasi": "ブラバントの歌"}]}, {"id": "P194", "property_midasi": {"ja": "立法府", "en": "legislative body", "type": "WikibaseItem"}, "entities": [{"id": "Q1137059", "entity_midasi": "連邦議会"}]}, {"id": "P92", "property_midasi": {"ja": "法的根拠", "en": "main regulatory text", "type": "WikibaseItem"}, "entities": [{"id": "Q633629", "entity_midasi": "ベルギー憲法"}]}, {"id": "P2936", "property_midasi": {"ja": "使用言語", "en": "language used", "type": "WikibaseItem"}, "entities": [{"id": "Q100103", "entity_midasi": "西フラマン語"}, {"id": "Q102172", "entity_midasi": "リンブルフ語"}, {"id": "Q2107617", "entity_midasi": "フラマン手話"}, {"id": "Q7411", "entity_midasi": "オランダ語"}, {"id": "Q9051", "entity_midasi": "ルクセンブルク語"}, {"id": "Q188", "entity_midasi": "ドイツ語"}, {"id": "Q150", "entity_midasi": "フランス語"}, {"id": "Q34024", "entity_midasi": "ピカルディ語"}, {"id": "Q34219", "entity_midasi": "ワロン語"}]}, {"id": "P2238", "property_midasi": {"ja": "公式シンボル", "en": "official symbol", "type": "WikibaseItem"}, "entities": [{"id": "Q130201", "entity_midasi": "ヒナゲシ"}]}, {"id": "P30", "property_midasi": {"ja": "大陸", "en": "continent", "type": "WikibaseItem"}, "entities": [{"id": "Q46", "entity_midasi": "ヨーロッパ"}]}, {"id": "P17", "property_midasi": {"ja": "国", "en": "country", "type": "WikibaseItem"}, "entities": [{"id": "Q31", "entity_midasi": "ベルギー"}]}, {"id": "P793", "property_midasi": {"ja": "重要な出来事", "en": "significant event", "type": "WikibaseItem"}, "entities": [{"id": "Q223933", "entity_midasi": "ベルギー独立革命"}, {"id": "Q1160895", "entity_midasi": "ロンドン条約"}]}, {"id": "P38", "property_midasi": {"ja": "通貨", "en": "currency", "type": "WikibaseItem"}, "entities": [{"id": "Q4916", "entity_midasi": "ユーロ"}, {"id": "Q232415", "entity_midasi": "ベルギー・フラン"}]}, {"id": "P463", "property_midasi": {"ja": "所属グループ", "en": "member of", "type": "WikibaseItem"}, "entities": [{"id": "Q458", "entity_midasi": "欧州連合"}, {"id": "Q1065", "entity_midasi": "国際連合"}, {"id": "Q7184", "entity_midasi": "北大西洋条約機構"}, {"id": "Q41550", "entity_midasi": "経済協力開発機構"}, {"id": "Q8908", "entity_midasi": "欧州評議会"}, {"id": "Q13116", "entity_midasi": "ベネルクス"}, {"id": "Q42262", "entity_midasi": "欧州宇宙機関"}, {"id": "Q7825", "entity_midasi": "世界貿易機関"}, {"id": "Q141720", "entity_midasi": "欧州航空輸送司令部"}, {"id": "Q1542735", "entity_midasi": "ベルギー＝ルクセンブルク経済同盟"}, {"id": "Q152299", "entity_midasi": "オランダ語連合"}, {"id": "Q151991", "entity_midasi": "ヨーロッパ南天天文台"}, {"id": "Q81299", "entity_midasi": "欧州安全保障協力機構"}, {"id": "Q191384", "entity_midasi": "国際復興開発銀行"}, {"id": "Q827525", "entity_midasi": "国際開発協会"}, {"id": "Q656801", "entity_midasi": "国際金融公社"}, {"id": "Q1043527", "entity_midasi": "多数国間投資保証機関"}, {"id": "Q899770", "entity_midasi": "投資紛争解決国際センター"}, {"id": "Q340195", "entity_midasi": "アフリカ開発銀行"}, {"id": "Q188822", "entity_midasi": "アジア開発銀行"}, {"id": "Q782942", "entity_midasi": "オーストラリア・グループ"}, {"id": "Q161549", "entity_midasi": "欧州石炭鉄鋼共同体"}, {"id": "Q1377612", "entity_midasi": "ヨーロッパ支払同盟"}, {"id": "Q663492", "entity_midasi": "欧州航空航法安全機構"}, {"id": "Q1928989", "entity_midasi": "オープン・スカイズ条約"}, {"id": "Q1072120", "entity_midasi": "大量破壊兵器の運搬手段であるミサイル及び関連汎用品・技術の輸出管理体制"}, {"id": "Q8475", "entity_midasi": "国際刑事警察機構"}, {"id": "Q1480793", "entity_midasi": "原子力供給国グループ"}, {"id": "Q842490", "entity_midasi": "化学兵器禁止機関"}, {"id": "Q3866537", "entity_midasi": "欧州機動調整センター"}, {"id": "Q521227", "entity_midasi": "統合装備協力機関"}, {"id": "Q233611", "entity_midasi": "国際水路機関"}, {"id": "Q826700", "entity_midasi": "国際エネルギー機関"}, {"id": "Q7809", "entity_midasi": "国際連合教育科学文化機関"}, {"id": "Q5611262", "entity_midasi": "地球観測に関する政府間会合"}, {"id": "Q17495", "entity_midasi": "万国郵便連合"}, {"id": "Q376150", "entity_midasi": "国際電気通信連合"}, {"id": "Q1969730", "entity_midasi": "シェンゲン圏"}, {"id": "Q1531570", "entity_midasi": "地球規模生物多様性情報機構"}]}], "title_en": "Belgium", "descriptions_en": "federal constitutional monarchy in Western Europe", "descriptions_ja": "西ヨーロッパに位置する国家", "aliases_ja": []}
```