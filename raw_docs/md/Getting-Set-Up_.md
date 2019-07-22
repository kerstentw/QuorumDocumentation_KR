## 셋업 및 퀵스타트

Quorum을 사용하기 위해서는 Quorum 노드와 Constellation/Tessera 노드를 설치하고 환경에 맞게 설정한 후
실행되어 있어야 합니다 (두 노드 모두 하단의 구축/설치 가이드를 참고하십시오). 키 생성, 제네시스 블록 및
Constellation/Tessera 구성 등 직접 Quorum을 셋업하기 위한 단계별 가이드를 곧 제공할 예정입니다. 현재로써
Quorum을 시작하기 위한 가장 좋은 방법은 Quorum Readme의
[Quickstart](https://github.com/jpmorganchase/quorum/#quickstart) 섹션에서도
설명했다시피 [Quorum
Examples](https://github.com/jpmorganchase/quorum-examples)를 실행하기 위해
만들어진 Vagrant 환경을 활용하는 것입니다. Vagrant 환경은 테스트 Quorum 네트워크를 자동적으로
셋팅하여 단 몇 분 만에 개발 가능한 상태로 구성하기 때문에 Quorum을 처음 사용하고자 할 때 권장드립니다.
Vagrant를 통하여 Quorum Examples 을 사용하는 대신 직접 Quorum을 셋업하고 싶다면 아래 내용을
참고해주세요. (참고: 본 문서화 작업은 진행중입니다.)

## 소스를 통한 Quorum 노드 빌드

Github에서 소스를 복사하여 빌드해보세요:

git clone <https://github.com/jpmorganchase/quorum.git>  
cd quorum  
make all

바이너리 파일은 $REPO\_ROOT/build/bin에 생성됩니다. geth와 bootnode를 쉽게 사용할 수 있도록 해당
폴더를 개인적으로 설정한 PATH로 이동하여, 바이너리 파일을 기존 PATH(e.g. /usr/local/bin)에
복사하십시오.

~/.bashrc 혹은 ~/.bash\_aliases파일에
PATH=$PATH:/path/to/repository/build/bin와 같이 생성한 바이너리 파일의 경로를 설정하면 보다
편리하게 사용할 수 있습니다.

테스트를 실행해보세요:

make test

## Constellation 설치하기

Constellation releases 페이지에서 여러분의 플랫폼에 맞는 패키지를 다운로드하신 후, 압축을 해제하십시오. 압축을
해제하여 나온 바이너리 파일을 설정한 PATH(e.g. /usr/local/bin)로 이동시키세요.

##   
  

## Tessera 설치하기

Tessera 프로젝트 페이지에 나와 있는 설치 가이드를 참고해주세요.

