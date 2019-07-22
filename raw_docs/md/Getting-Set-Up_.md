<span lang="zh-CN">셋업 및 퀵스타트</span>
------------------------------------------

Quorum<span lang="zh-CN">을 사용하기 위해서는 </span>Quorum <span lang="zh-CN">노드와 </span>Constellation/Tessera <span lang="zh-CN">노드를 설치하고 환경에 맞게 설정한 후 실행되어 있어야 합니다 </span>(<span lang="zh-CN">두 노드 모두 하단의 구축</span>/<span lang="zh-CN">설치 가이드를 참고하십시오</span>). <span lang="zh-CN">키 생성</span>, <span lang="zh-CN">제네시스 블록 및 </span>Constellation/Tessera <span lang="zh-CN">구성 등 직접 </span>Quorum<span lang="zh-CN">을 셋업하기 위한 단계별 가이드를 곧 제공할 예정입니다</span>. <span lang="zh-CN">현재로써 </span>Quorum<span lang="zh-CN">을 시작하기 위한 가장 좋은 방법은 </span>Quorum Readme<span lang="zh-CN">의 </span>[Quickstart](https://github.com/jpmorganchase/quorum/#quickstart) <span lang="zh-CN">섹션에서도 설명했다시피 </span>[Quorum Examples](https://github.com/jpmorganchase/quorum-examples)<span lang="zh-CN">를 실행하기 위해 만들어진 </span>Vagrant <span lang="zh-CN">환경을 활용하는 것입니다</span>. Vagrant <span lang="zh-CN">환경은 테스트 </span>Quorum <span lang="zh-CN">네트워크를 자동적으로 셋팅하여 단 몇 분 만에 개발 가능한 상태로 구성하기 때문에 </span>Quorum<span lang="zh-CN">을 처음 사용하고자 할 때 권장드립니다</span>. Vagrant<span lang="zh-CN">를 통하여 </span>Quorum Examples <span lang="zh-CN">을 사용하는 대신 직접 </span>Quorum<span lang="zh-CN">을 셋업하고 싶다면 아래 내용을 참고해주세요</span>. (<span lang="zh-CN">참고</span>: <span lang="zh-CN">본 문서화 작업은 진행중입니다</span>.)

<span lang="zh-CN">소스를 통한 </span>Quorum <span lang="zh-CN">노드 빌드</span>
--------------------------------------------------------------------------------

Github<span lang="zh-CN">에서 소스를 복사하여 빌드해보세요</span>:

git clone <https://github.com/jpmorganchase/quorum.git>
cd quorum
make all

<span lang="zh-CN">바이너리 파일은 </span>$REPO\_ROOT/build/bin<span lang="zh-CN">에 생성됩니다</span>. geth<span lang="zh-CN">와 </span>bootnode<span lang="zh-CN">를 쉽게 사용할 수 있도록 해당 폴더를 개인적으로 설정한 </span>PATH<span lang="zh-CN">로 이동하여</span>, <span lang="zh-CN">바이너리 파일을 기존 </span>PATH(e.g. /usr/local/bin)<span lang="zh-CN">에 복사하십시오</span>.

~/.bashrc <span lang="zh-CN">혹은 </span>~/.bash\_aliases<span lang="zh-CN">파일에 </span>PATH=$PATH:/path/to/repository/build/bin<span lang="zh-CN">와 같이 생성한 바이너리 파일의 경로를 설정하면 보다 편리하게 사용할 수 있습니다</span>.

<span lang="zh-CN">테스트를 실행해보세요</span>:

make test

Constellation <span lang="zh-CN">설치하기</span>
------------------------------------------------

<span id="_heading=h.gjdgxs"></span> Constellation releases <span lang="zh-CN">페이지에서 여러분의 플랫폼에 맞는 패키지를 다운로드하신 후</span>, <span lang="zh-CN">압축을 해제하십시오</span>. <span lang="zh-CN">압축을 해제하여 나온 바이너리 파일을 설정한 </span>PATH(e.g. /usr/local/bin)<span lang="zh-CN">로 이동시키세요</span>.

Tessera <span lang="zh-CN">설치하기</span>
------------------------------------------

Tessera <span lang="zh-CN">프로젝트 페이지에 나와 있는 설치 가이드를 참고해주세요</span>.
