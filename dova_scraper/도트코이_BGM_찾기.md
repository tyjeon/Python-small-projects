# 도트코이 BGM을 찾아내기까지의 과정

## 요약
* 내가 찾으려 했던 음악은 바닐라ヴァニラ라는 곡이다.
    * * http://musmus.main.jp/music_game_03.html
* **tyrano engine은 압축 파일이라 반디집으로 열린다.**
* data/bgm에 있는 **nakamura.ogg** 가 내가 찾던 음악이다.
    * 이 노래의 길이는 02:15이다.
* 같은 폴더에 **kyuujitu1.ogg** 이라는 bgm이 watson의 orange라는 곡이었다. (알송으로 열어서 알음)
* 이 노래는 **musmus** 사이트에 있다.
* musmus 사이트 우상단 구글서치에 orange라고 검색했다.
* 각 결과 페이지를 하나씩 들어가보며 길이가 **02:15** 인 파일을 찾는다.
* 이렇게 찾았다.
* 교훈 : **일단 헥스로 편집하기 전에 압축파일인지 확인해본다.**

## 음악을 찾기까지
* 도트코이 한글판을 [공식 사이트](http://kuro.kilo.jp/dotokoi/#dl)에서 받았다.
    * [자주 묻는 질문의 음악 부분](http://kuro.kilo.jp/dotokoi/#qa)에서 음악 소재는 거의 ED 크레딧에 써있는대로이며 BGM은 [dova-s](http://dova-s.jp/)에서 받았다고 적어놨었다.
* dova-s 스크레이핑
    * 게임을 실행해서 내가 원하는 부분을 스톱워치로 시간을 쟀다. 대충 02:14~02:17이었다.
    * **dova-s에서 음악 길이가 02:14~02:17인 음악을 전부 찾는 기능을 가진** dova_scraper.py 를 만들었다.
    * 유튜브 링크를 전부 받은 뒤, **youtube-dl** 로 모든 파일을 받았다.
    * 알송으로 3~5초씩 들으며 넘겼다. 없었다.
    * 혹시나 싶어 2분~2분 30초 구간 전부를 다시 스크레이핑하고 다운로드받고 하나씩 들어봤지만 역시 없었다.
* 魔王魂 사이트
    * **음악 소재는 거의 ED 크레딧에 써있는대로** 라고 사이트에서 언급했기 때문에, 엔딩을 봤는데 **MUSMUS님, 魔王魂님** 이라고 적혀 있었다.
    * [이 분 사이트](https://maoudamashii.jokersounds.com/)로 갔다.
    * 이 분은 모든 무료 곡을 한 번에 받을 수 있게 zip 링크를 제공해서 모두 받아서 길이가 2분대인 음악을 들어보았다. 없었다.
* 언패킹
    * 게임을 열어보기로 했다.
    * 이 게임은 [Tyrano engine으로 만들어졌으며](https://namu.wiki/w/%EB%8F%84%ED%8A%B8%EC%BD%94%EC%9D%B4), 이를 언팩하기 위해 [tyrano unpacker에 대한 글](https://www.vg-resource.com/thread-32244.html)을 찾았다. dragon unpacker를 썼다고 했는데, 안 되더라.
    * 그래서 ollydbg와 cheat engine을 써서 mp3에 대한 내용을 찾아봤으나 없었다.
    * HxD로 열어서 음악파일을 찾아보면 있지 않을까 싶어 도트코이.exe 파일을 열었는데, data/bgm 이라는 텍스트를 찾아냈다.
    * 혹시나 싶어서 반디집으로 열어봤는데 열렸다.
    * data/bgm에 ogg 파일이 있었고, 이 중에 nakamura.ogg가 내가 원하던 파일이었다.
    * 같은 폴더에 .DS_STORE 라는 파일이 있어 찾아보았고 이를 [언패킹하는 소스](https://github.com/gehaxelt/Python-dsstore)를 찾았다.
    * 파일 사용법을 몰라 아래 코드를 적당히 바꿔서 실행했다.
    ```python
    if len(sys.argv) < 2:
        sys.exit("Usage: python main.py <DS_STORE FILE>")
    if not os.path.exists(sys.argv[1]):
        sys.exit("File not found: Usage main.py <file>")
    with open(sys.argv[1], "rb") as f:
        d = dsstore.DS_Store(f.read(), debug=False)
        files = d.traverse_root()
        print("Count: ", len(files))
        for f in files:
            print(f)
    ```
    이걸 이렇게 바꿨다.
    ```python
    with open(".DS_STORE", "rb") as f:
        d = dsstore.DS_Store(f.read(), debug=False)
        files = d.traverse_root()
        print("Count: ", len(files))
        for f in files:
            print(f)
    ```
    * 이렇게 해서 .DS_STORE의 파일 내용을 확인했지만 그냥 파일 이름 목록이었고 별 소득은 없었다.
* 끝
    * 알송으로 파일을 열어보니 일부는 파일 태그가 지워지지 않은 상태였다.
    * 그 중에 watson - orange라는 곡을 검색해보니 musmus 사이트로 연결되었다.
    * 사이트 우상단 구글서치에 orange라고 검색하고, 나온 결과 페이지 중에 "게임" 분류인 페이지로 들어가서 길이가 02:15인 음악을 찾아보았다.
    * 있었다. 찾기까지 5시간정도 걸렸다.
