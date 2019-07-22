<span lang="zh-CN">기초부터 시작하기 </span>
============================================

Raft <span lang="zh-CN">합의 알고리즘의 쿼럼</span>
---------------------------------------------------

1.  \[\[<span lang="zh-CN">셋업하기</span>|<span lang="zh-CN">셋업하기</span>\]\] <span lang="zh-CN">섹션에서 설명하는대로 </span>Quorum<span lang="zh-CN">을 빌딩하십시오</span>. PATH<span lang="zh-CN">에 </span>geth<span lang="zh-CN">와 </span>bootnode<span lang="zh-CN">가 있는지 확인하십시오</span>.

2.  <span lang="zh-CN">새 노드의 기반이 될 작업 디렉토리를 만들고 변경하십시오</span>.

3.  <span lang="zh-CN">이 노드를 위해 </span>geth<span lang="zh-CN">를 사용하여 한 개 이상의 계정을 만들고 </span>(--datadir new-node-1 account new) <span lang="zh-CN">계정 주소를 제거하십시오</span>. <span lang="zh-CN">하고자 하는 것에 따라 자금이 있는 계좌가 필요할 수 있습니다</span>.

4.  genesis.json <span lang="zh-CN">파일을 만드십시오</span>. <span lang="zh-CN">[여기](https://github.com/jpmorganchase/quorum-examples/blob/master/examples/7nodes/genesis.json)에 예제가 있습니다</span>. <span lang="zh-CN">이전 단계에서 생성한 계정으로 </span>alloc <span lang="zh-CN">필드를 미리 입력해야 합니다</span>.

5.  <span lang="zh-CN">노드 키 </span>bootnode <span lang="zh-CN">생성 </span>(--genkey=nodekey)<span lang="zh-CN">하고 </span>datadir<span lang="zh-CN">에 복사</span>

6.  bootnode --nodekey=new-node-1/nodekey --writeaddress <span lang="zh-CN">를 실행하고 표시된 아웃풋을 기록하십시오</span>. <span lang="zh-CN">이것은 새로운 노드의 </span>enode <span lang="zh-CN">아이디입니다</span>.

7.  static-nodes.json<span lang="zh-CN">라는 파일을 만들고 [예제](https://github.com/jpmorganchase/quorum-examples/blob/master/examples/7nodes/permissioned-nodes.json)와 일치하도록 편집하십시오</span>. <span lang="zh-CN">파일에는 </span>enode id<span lang="zh-CN">오</span>devp2p <span lang="zh-CN">및 </span>raft<span lang="zh-CN">에 사용할 포트가 있는 노드에 대한 라인이 하나 있어야 합니다</span>. <span lang="zh-CN">이 파일이 노드 데이터 디렉토리에 있는지 확인하십시오</span>.

8.  geth<span lang="zh-CN">로 새로운 노드를 초기화하십시오 </span>--datadir new-node-1 init genesis.json

9.  <span lang="zh-CN">노드를 시작하고 다음을 통해 백그라운드로 보내십시오</span>. PRIVATE\_CONFIG=ignore nohup geth --datadir new-node-1 --nodiscover --verbosity 5 --networkid 31337 --raft --raftport 50000 --rpc --rpcaddr 0.0.0.0 --rpcport 22000 --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,raft --emitcheckpoints --port 21000 2&gt;&gt;node.log &

<span lang="zh-CN">당신의 노드는 이제 작동 가능하며 </span>geth attach new-node-1/geth.ipc<span lang="zh-CN">를 연결할 수 있습니다</span>. <span lang="zh-CN">이 구성은 프리픽스 </span>PRIVATE\_CONFIG=ignore<span lang="zh-CN">에서 확인할 수 있는 것처럼 프라이버시 서포트 없이 </span>Quorum<span lang="zh-CN">을 시작합니다</span>. \[\[<span lang="zh-CN">프라이버시 트랜잭션 매니저로 프라이버시 지원 방법</span>|<span lang="zh-CN">기초부터</span>\#adding-privacy-transaction-manager\]\] <span lang="zh-CN">섹션을 참조하십시오</span>.

### <span lang="zh-CN">노드 추가하기</span>

1.  <span lang="zh-CN">앞의 가이드의 </span>1, 2, 5, 6<span lang="zh-CN">단계를 완료하십시오</span>.

2.  <span lang="zh-CN">현재 체인인 </span>genesis.json <span lang="zh-CN">및 </span>static-nodes.json.json<span lang="zh-CN">를 회수하십시오</span>. static-nodes.json <span lang="zh-CN">은 노드 </span>data dir<span lang="zh-CN">에 배치되어야 합니다</span>.

3.  geth<span lang="zh-CN">로 새로운 노드를 초기화 하십시오 </span>--datadir new-node-2 init genesis.json

4.  static-nodes.json<span lang="zh-CN">을 편집하고 구성중인 새 노드에 대한 새로운 항목을 추가하십시오 </span>(<span lang="zh-CN">마지막에 있어야 함</span>)

5.  <span lang="zh-CN">이미 실행중인 체인 노드에 연결하고 실행합니다</span>.

6.  raft.addPeer('enode://new-nodes-enode-address-from-step-6-of-the-above@127.0.0.1:21001?discport=0&raftport=50001')

7.  <span lang="zh-CN">노드를 시작하고 다음을 통해 백그라운드로 보내십시오</span>. PRIVATE\_CONFIG=ignore nohup geth --datadir new-node-2 --nodiscover --verbosity 5 --networkid 31337 --raft --raftport 50001 --raftjoinexisting RAFT\_ID --rpc --rpcaddr 0.0.0.0 --rpcport 22001 --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,raft --emitcheckpoints --port 21001 2&gt;&gt;node.log &. <span lang="zh-CN">여기서 </span>RAFT\_ID<span lang="zh-CN">는 </span>5<span lang="zh-CN">단계의 </span>raft.addPeer() <span lang="zh-CN">커맨드에 대한 응답입니다</span>.

8.  <span lang="zh-CN">옵션</span>: <span lang="zh-CN">다른 모든 체인 참여자들과 새로운 </span>static-nodes.json<span lang="zh-CN">를 공유합니다</span>.

<span lang="zh-CN">추가 노드는 이제 작동가능하며 이전에 설정된 노드와 동일한 체인의 일부입니다</span>.

### <span lang="zh-CN">노드 제거</span>

<span lang="zh-CN">체인의 이미 실행중인 노드에 연결하고 </span>raft.cluster<span lang="zh-CN">를 실행하여 제거해야 하는 노드에 해당하는 </span>RAFT\_ID<span lang="zh-CN">를 가져옵니다</span>.

raft.removePeer(RAFT\_ID)<span lang="zh-CN">를 실행하십시오</span>.

<span lang="zh-CN">제거된 노드에 해당하는 </span>geth <span lang="zh-CN">프로세스를 중지하십시오</span>.

<span lang="zh-CN">이스탄불 </span>BFT <span lang="zh-CN">합의 알고리즘의 </span>Quorum
---------------------------------------------------------------------------------------

\[\[<span lang="zh-CN">셋업하기</span>|<span lang="zh-CN">셋업하기</span>\]\]<span lang="zh-CN">에서 설명한대로 </span>Quorum<span lang="zh-CN">을 빌딩하십시오</span>. PATH<span lang="zh-CN">에 </span>geth<span lang="zh-CN">와 </span>bootnode<span lang="zh-CN">가 있는지 확인하십시오</span>.

[istanbul-tools](https://github.com/jpmorganchase/istanbul-tools) <span lang="zh-CN">를 설치하고 </span>PAT<span lang="zh-CN">에 이스탄불 바이너리를 넣으세요</span>.

X<span lang="zh-CN">개의 초기 유효성 검사기 노드 각각에 대한 작업 디렉토리를 만듭니다</span>.

<span lang="zh-CN">노드의 작업 디렉토리 중 선두에 있는</span>(<span lang="zh-CN">선두라고 생각하는 것</span>) <span lang="zh-CN">노드로 변경하고 </span>istanbul setup<span lang="zh-CN">을 실행하여 </span>X <span lang="zh-CN">초기 유효성 검사 노드를 위한 셋업 파일들을 생성합니다</span>. setup --num X --nodes --quorum --save --verbose <span lang="zh-CN">**이 명령은** </span>**X**<span lang="zh-CN">**번이 아니라 한 번만 실행합니다**</span>**.** <span lang="zh-CN">이 커맨드는 </span>0<span lang="zh-CN">에서 </span>X-1<span lang="zh-CN">까지의 번호가 지정된 디렉토리에 있는 모든 초기 유효성 검사기 노드에 대해 </span>tatic-nodes.json, genesis.json, <span lang="zh-CN">및 </span>nodekeys<span lang="zh-CN">와 같은 몇 가지 항목을 생성합니다</span>.

<span lang="zh-CN">모든 초기 유효성 검사 노드의 의도된 </span>IP <span lang="zh-CN">및 포트 번호를 포함하도록 </span>static-nodes.json<span lang="zh-CN">을 갱신하십시오</span>. static-nodes.json<span lang="zh-CN">에서는 각 노드마다 다른 행이 표시됩니다</span>. <span lang="zh-CN">설치 가이드의 나머지 부분에서 </span>Y<span lang="zh-CN">행은 </span>Y<span lang="zh-CN">노드를 말하고 행 </span>1<span lang="zh-CN">은 리드 노드에 해당한다고 가정합니다</span>.

<span lang="zh-CN">각 노드의 작업 디렉토리에서 </span>data<span lang="zh-CN">라는 데이터 디렉토리를 만들고 </span>data <span lang="zh-CN">내부에는 </span>geth <span lang="zh-CN">디렉토리를 생성합니다</span>.

<span lang="zh-CN">이제 필요한 노드의 작업 디렉토리에서 </span>--datadir data account<span lang="zh-CN">를 실행하여 모든 노드에 대한 초기 계정을 생성합니다</span>. <span lang="zh-CN">결과적으로 터미널에 나타난 퍼블릭 계정 주소를 기록해야 합니다</span>. <span lang="zh-CN">필요한 만큼 이를 반복하십시오</span>. <span lang="zh-CN">하고자 하는 바에 따라 자금이 있는 계좌가 필요할 수 있습니다</span>.

<span lang="zh-CN">초기 블록에 계정을 추가하려면 리드 노드의 작업 디렉토리에서 </span>genesis.json<span lang="zh-CN">파일을 편집하고 이전 단계에서 생성된 계정으로 </span>alloc <span lang="zh-CN">필드를 업데이트 하십시오</span>.

<span lang="zh-CN">다음으로 현재 리드 노드의 작업 디렉토리에 있는 파트 </span>4<span lang="zh-CN">에서 생성된 파일을 다른 모든 노드에 배포해야 합니다</span>. <span lang="zh-CN">이렇게 하려면 </span>genesis.json<span lang="zh-CN">을 모든 노드의 작업 디렉토리에 두고 각 노드의 데이터 폴더에 </span>static-nodes.json<span lang="zh-CN">을 놓고 </span>X/nodekey <span lang="zh-CN">를 </span>(X-1)<span lang="zh-CN">의 </span>data/geth <span lang="zh-CN">디렉토리에 위치시킵니다</span>.

<span lang="zh-CN">리드노드의 작업 디렉토리로 전환하고 </span>geth --datadir data init genesis.json<span lang="zh-CN">으로 초기화하십시오</span>. 3<span lang="zh-CN">단계에서 생성된 모든 작업 디렉토리 </span>X<span lang="zh-CN">에 대해 반복하십시오</span>. geth init<span lang="zh-CN">*을 실행하여 얻은 해시는 모든 노드와 일치해야 합니다*</span>*.*

<span lang="zh-CN">모든 노드를 시작하고 다음을 통해 백그라운드로 보냅니다</span>: PRIVATE\_CONFIG=ignore nohup geth --datadir data --permissioned --nodiscover --istanbul.blockperiod 5 --syncmode full --mine --minerthreads 1 --verbosity 5 --networkid 10 --rpc --rpcaddr 0.0.0.0 --rpcport YOUR\_NODES\_RPC\_PORT\_NUMBER --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,istanbul --emitcheckpoints --port YOUR\_NODES\_PORT\_NUMBER 2&gt;&gt;node.log

<span lang="zh-CN">그리고 </span>YOUR\_NODES\_RPC\_PORT\_NUMBER <span lang="zh-CN">및 </span>YOUR\_NODES\_PORT\_NUMBER<span lang="zh-CN">을 노드의 지정된 포트 번호로 바꾸십시오</span>. YOUR\_NODES\_PORT\_NUMBER<span lang="zh-CN">은 파트 </span>5<span lang="zh-CN">에서 결정된 이 노드의 포트 번호와 일치해야 합니다</span>.

<span lang="zh-CN">이제 노드가 작동하며 </span>geth attach data/geth.ipc<span lang="zh-CN">를 연결할 있습니다</span>. <span lang="zh-CN">이 구성은 프리픽스 </span>PRIVATE\_CONFIG=ignore<span lang="zh-CN">에서 확인할 수 있는 것처럼 프라이버시 지원이 없는 쿼럼을 시작합니다</span>. <span lang="zh-CN">하단의 </span>\[\[<span lang="zh-CN">프라이버시 트랜잭션 매니저를 이용한 프라이버시 지원 방법</span>|<span lang="zh-CN">기초부터 시작하기</span>\#<span lang="zh-CN">프라이버시</span>-<span lang="zh-CN">트랜잭션</span>-<span lang="zh-CN">매니저 추가하기</span>\]\] <span lang="zh-CN">섹션을 참조하십시오</span>.

<span lang="zh-CN">이스탄불 툴은 </span>X<span lang="zh-CN">개의 노드를 생성하는데 사용될 수 있으며 자세한 정보는 </span>[docs](https://github.com/jpmorganchase/istanbul-tools)<span lang="zh-CN">에서 확인할 수 있습니다</span>.

### <span lang="zh-CN">검증자</span>(Validator) <span lang="zh-CN">추가하기</span>

<span lang="zh-CN">추가해야 할 새로운 노드의 작업 디렉토리를 만듭니다</span>.

<span lang="zh-CN">새 노드의 작업 디렉토리로 변경하고 </span>istanbul setup --num 1 --verbose --quorum --save<span lang="zh-CN">를 실행합니다</span>. <span lang="zh-CN">그러면 </span>Address, NodeInfo <span lang="zh-CN">및 </span>genesis.json<span lang="zh-CN">을 포함하여 검증자의 세부 정보가 생성됩니다</span>. <span lang="zh-CN">검증자의 주소를 복사하고 현재 검증자의 절반 이상에서 </span>istanbul.propose(&lt;address&gt;, true)<span lang="zh-CN">를 실행합니다</span>.

istanbul.getValidators()<span lang="zh-CN">를 실행하여 새로운 검증자가 검증자 목록에 추가되었는지 확인합니다</span>.

\[\[<span lang="zh-CN">셋업하기</span>|<span lang="zh-CN">셋업하기</span>\]\] <span lang="zh-CN">섹션에서 설명한대로 </span>Quorum<span lang="zh-CN">을 빌딩하십시오</span>. PATH<span lang="zh-CN">에 </span>geth<span lang="zh-CN">가 있는지 확인하십시오</span>. <span lang="zh-CN">기존 체인에서 </span>static-nodes.json <span lang="zh-CN">및 </span>genesis.json<span lang="zh-CN">을 복사하십시오</span>. static-nodes.json<span lang="zh-CN">은 새로운 노드 </span>data dir<span lang="zh-CN">에 배치되어야 합니다</span>.

static-nodes.json<span lang="zh-CN">을 편집하고 새로운 검증자 노드 정보를 파일의 끝에 추가하십시오</span>. <span lang="zh-CN">새로운 검증자 노드 정보는 </span>2<span lang="zh-CN">단계에서 실행된 </span>istanbul setup --num 1 --verbose --quorum --save <span lang="zh-CN">커맨드의 결과물에서 얻을 수 있습니다</span>. <span lang="zh-CN">노드 정보의 </span>IP<span lang="zh-CN">주소와 포트를 사용하고자 하는 검증자와 포트의 </span>IP <span lang="zh-CN">주소와 일치하도록 업데이트하십시오</span>.

istanbul setup <span lang="zh-CN">커맨드로 생성된 노드키를 작업 디렉토리의 </span>geth <span lang="zh-CN">디렉토리에 복사하십시오</span>.

geth --datadir new-node-1 account new<span lang="zh-CN">를 사용하여 이 노드에 대해 하나 이상의 계정을 생성하고 계정 주소를 제거하십시오</span>.

geth --datadir new-node-1 init genesis.json<span lang="zh-CN">를 사용하여 새로운 노드를 초기화하십시오</span>.

<span lang="zh-CN">노드를 시작하고 </span>PRIVATE\_CONFIG=ignore nohup geth --datadir data --permissioned --nodiscover --istanbul.blockperiod 5 --syncmode full --mine --minerthreads 1 --verbosity 5 --networkid 10 --rpc --rpcaddr 0.0.0.0 --rpcport YOUR\_NODES\_RPC\_PORT\_NUMBER --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,istanbul --emitcheckpoints --port YOUR\_NODES\_PORT\_NUMBER 2&gt;&gt;node.log<span lang="zh-CN">를 이용하여 백그라운드로 보내십시오</span>. <span lang="zh-CN">그리고 </span>YOUR\_NODES\_RPC\_PORT\_NUMBER <span lang="zh-CN">및 </span>YOUR\_NODES\_PORT\_NUMBER<span lang="zh-CN">를 지정된 포트 번호로 바꾸십시오</span>. YOUR\_NODES\_PORT\_NUMBER<span lang="zh-CN">은 파트 </span>7<span lang="zh-CN">에서 결정된 이 노드의 포트 번호와 일치해야 합니다</span>.

### <span lang="zh-CN">검증자 제거하기</span>

<span lang="zh-CN">실행중인 검증자에 연결하고 </span>istanbul.getValidators()<span lang="zh-CN">를 실행하고 제거해야하는 검증자의 주소를 확인하십시오</span>.

<span lang="zh-CN">현 검증자의 절반 이상에서 제거해야 하는 검증자의 주소를 전달하여 </span>istanbul.propose(&lt;address&gt;, false)<span lang="zh-CN">를 실행하십시오</span>.

istanbul.getValidators()<span lang="zh-CN">를 실행하여 검증자가 제거되었는지 확인하십시오</span>.

<span lang="zh-CN">제거된 검증자에 해당하는 </span>geth <span lang="zh-CN">프로세스를 중지하십시오</span>.

### <span lang="zh-CN">비검증자 노드 추가하기</span>

<span lang="zh-CN">추가해야 할 새로운 노드의 작업 디렉토리를 만드십시오</span>.

<span lang="zh-CN">새로운 노드의 작업 디렉토리로 변경하고 </span>istanbul setup --num 1 --verbose --quorum --save<span lang="zh-CN">를 실행하십시오</span>. <span lang="zh-CN">그러면 </span>Address, NodeInfo and genesis.json<span lang="zh-CN">을 포함한 노드의 세부정보가 생성됩니다</span>.

\[\[<span lang="zh-CN">셋업하기</span>|<span lang="zh-CN">셋업하기</span>\]\] <span lang="zh-CN">섹션에서 설명한대로 </span>Quorum<span lang="zh-CN">을 빌딩하십시오</span>. PATH<span lang="zh-CN">에 </span>geth<span lang="zh-CN">가 있는지 확인하십시오</span>.

<span lang="zh-CN">기존 체인에서 </span>static-nodes.json <span lang="zh-CN">및 </span>genesis.json<span lang="zh-CN">을 복사하십시오</span>. static-nodes.json<span lang="zh-CN">은 새로운 노드 </span>data dir<span lang="zh-CN">에 배치되어야 합니다</span>.

static-nodes.json<span lang="zh-CN">을 편집하고 새로운 노드 정보를 파일의 끝에 추가하십시오</span>. <span lang="zh-CN">새로운 노드 정보는 </span>2<span lang="zh-CN">단계에서 실행된 </span>istanbul setup --num 1 --verbose --quorum --save <span lang="zh-CN">커맨드의 결과물에서 얻을 수 있습니다</span>. <span lang="zh-CN">노드 정보의 </span>IP<span lang="zh-CN">주소와 포트를 사용하고자 하는 검증자와 포트의 </span>IP <span lang="zh-CN">주소와 일치하도록 업데이트하십시오</span>.

istanbul setup <span lang="zh-CN">커맨드로 생성된 노드키를 작업 디렉토리의 </span>geth <span lang="zh-CN">디렉토리에 복사하십시오</span>.

geth --datadir new-node-1 account new<span lang="zh-CN">를 사용하여 이 노드에 대해 하나 이상의 계정을 생성하고 계정 주소를 제거하십시오</span>.

geth --datadir new-node-1 init genesis.json<span lang="zh-CN">를 사용하여 새로운 노드를 초기화하십시오</span>.

<span lang="zh-CN">노드를 시작하고 </span>PRIVATE\_CONFIG=ignore nohup geth --datadir data --permissioned --nodiscover --istanbul.blockperiod 5 --syncmode full --verbosity 5 --networkid 10 --rpc --rpcaddr 0.0.0.0 --rpcport YOUR\_NODES\_RPC\_PORT\_NUMBER --rpcapi admin,db,eth,debug,net,shh,txpool,personal,web3,quorum,istanbul --emitcheckpoints --port YOUR\_NODES\_PORT\_NUMBER 2&gt;&gt;node.log<span lang="zh-CN">를 이용하여 백그라운드로 보내십시오</span>. <span lang="zh-CN">그리고 </span>YOUR\_NODES\_RPC\_PORT\_NUMBER <span lang="zh-CN">및 </span>YOUR\_NODES\_PORT\_NUMBER<span lang="zh-CN">를 지정된 포트 번호로 바꾸십시오</span>. YOUR\_NODES\_PORT\_NUMBER<span lang="zh-CN">은 </span>5<span lang="zh-CN">단계에서 결정된 이 노드의 포트 번호와 일치해야 합니다</span>.

### <span lang="zh-CN">비검증자 노드 제거하기 </span>

<span lang="zh-CN">제거해야 할 노드에 해당하는 </span>geth <span lang="zh-CN">프로세스를 중지하십시오</span>.

Clique <span lang="zh-CN">합의 알고리즘의 </span>Quorum
-------------------------------------------------------

<span lang="zh-CN">프라이버시 트랜잭션 매니저 추가하기</span>
=============================================================

Tessera
-------

Quorum<span lang="zh-CN">을 빌딩하고 </span>\[\[<span lang="zh-CN">셋업하기</span>|<span lang="zh-CN">셋업하기</span>\]\] <span lang="zh-CN">섹션에서 설명하는 대로 </span>[Tessera](https://github.com/jpmorganchase/tessera/releases)<span lang="zh-CN">를 설치하십시오</span>. PATH<span lang="zh-CN">에 </span>geth<span lang="zh-CN">와 </span>bootnode<span lang="zh-CN">가 포함되어 있는지 확인하십시오</span>. tessera.jar <span lang="zh-CN">릴리스 파일의 위치를 알고 있어야 합니다</span>.

java -jar /path-to-tessera/tessera.jar -keygen -filename new-node-1<span lang="zh-CN">를 사용하여 새 키들을 생성하십시오</span>.

<span lang="zh-CN">새롭게 생성된 키가 참조된 [샘플](https://github.com/jpmorganchase/tessera/wiki/Sample-configuration)</span>[1](https://github.com/jpmorganchase/tessera/wiki/Sample-configuration)<span lang="zh-CN">과 [샘플](https://github.com/jpmorganchase/quorum-examples/blob/master/examples/7nodes/tessera-init.sh)</span>[2](https://github.com/jpmorganchase/quorum-examples/blob/master/examples/7nodes/tessera-init.sh)<span lang="zh-CN">를 참조하여 새로운 구성 파일을 만드십시오</span>. <span lang="zh-CN">파일 이름을 기록하거나 이 예제에서와 같이 파일 이름을 </span>config.json<span lang="zh-CN">로 하십시오</span>.

tessera <span lang="zh-CN">노드를 시작하고 </span>java -jar /path-to-tessera/tessera.jar -configfile config.json &gt;&gt; tessera.log 2&gt;&1 &<span lang="zh-CN">를 통해 백그라운드로 보내십시오</span>.

<span lang="zh-CN">노드를 시작하고 </span>PRIVATE\_CONFIG=tm.ipc nohup geth --datadir new-node-1 --nodiscover --verbosity 5 --networkid 31337 --raft --raftport 50000 --rpc --rpcaddr 0.0.0.0 --rpcport 22000 --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,raft --emitcheckpoints --port 21000 2&gt;&gt;node.log &<span lang="zh-CN">를 통해 백그라운드로 보내십시오</span>.

<span lang="zh-CN">당신의 노드는 이제 작동 가능하며 </span>attach new-node-1/geth.ipc<span lang="zh-CN">를 통해 연결할 수 있습니다</span>. Tessera IPC <span lang="zh-CN">브릿지는 일반적으로 프리픽스 </span>PRIVATE\_CONFIG=tm.ipc<span lang="zh-CN">에 나와 있는 것처럼 </span>tm.ipc<span lang="zh-CN">라는 이름으로 </span>config.json<span lang="zh-CN">에 정의된 파일 이름 위에 있습니다</span>. <span lang="zh-CN">이제 노드가 프라이빗 트랜잭션을 주고 받을 수 있고 퍼블릭 노드키는 </span>new-node-1.pub <span lang="zh-CN">파일에 있게 됩니다</span>. Tessera<span lang="zh-CN">는 구성에 있어서 많은 유연성을 제공합니다</span>. [Tessera wiki](https://github.com/jpmorganchase/tessera/wiki)<span lang="zh-CN">에서 완벽한 최신 구성 옵션을 확인하십시오</span>.

Constellation
-------------

Quorum<span lang="zh-CN">을 빌딩하고 </span>\[\[<span lang="zh-CN">셋업하기</span>|<span lang="zh-CN">셋업하기</span>\]\] <span lang="zh-CN">섹션에서 설명한 바와 같이 </span>[Constellation](https://github.com/jpmorganchase/constellation/releases)<span lang="zh-CN">을 설치하십시오</span>. PATH<span lang="zh-CN">에 </span>geth, bootnode <span lang="zh-CN">및 </span>constellation <span lang="zh-CN">노드 바이너리가 있는지 확인하십시오</span>.

constellation-node --generatekeys=new-node-1<span lang="zh-CN">로 새로운 키들을 생성하십시오</span>.

constellation <span lang="zh-CN">노드를 시작하고 다음을 통해 백그라운드로 보내십시오</span>: constellation-node --url=https://127.0.0.1:9001/ --port=9001 --workdir=. --socket=tm.ipc --publickeys=new-node-1.pub --privatekeys=new-node-1.key --othernodes=https://127.0.0.1:9001/ &gt;&gt; constellation.log 2&gt;&1 &

Start your node and send it into background with PRIVATE\_CONFIG=tm.ipc nohup geth --datadir new-node-1 --nodiscover --verbosity 5 --networkid 31337 --raft --raftport 50000 --rpc --rpcaddr 0.0.0.0 --rpcport 22000 --rpcapi admin,db,eth,debug,miner,net,shh,txpool,personal,web3,quorum,raft --emitcheckpoints --port 21000 2&gt;&gt;node.log &

<span lang="zh-CN">당신의 노드는 이제 작동 가능하며 </span>attach new-node-1/geth.ipc<span lang="zh-CN">를 통해 연결할 수 있습니다</span>. Constellation IPC bridge<span lang="zh-CN">는 당신의 설정에 정의된 파일 이름 위에 있을 것입니다</span>. <span lang="zh-CN">위의 </span>3<span lang="zh-CN">번 단계에서 </span>--socket=file-name.ipc <span lang="zh-CN">옵션을 보십시오</span>. <span lang="zh-CN">이제 노드가 프라이빗 트랜잭션을 주고 받을 수 있고 퍼블릭 노드키는 </span>new-node-1.pub <span lang="zh-CN">파일에 있게 됩니다</span>.

<span lang="zh-CN">허가형 구성 사용하기 </span>
===============================================

Quorum<span lang="zh-CN">은 사용자 지정 화이트리스트를 기반으로 허가형 시스템을 함께 제공합니다</span>. <span lang="zh-CN">자세한 설명은 </span>[Network Permissioning](https://github.com/jpmorganchase/quorum/wiki/Security#network-permissioning)<span lang="zh-CN">에서 확인할 수 있습니다</span>.
