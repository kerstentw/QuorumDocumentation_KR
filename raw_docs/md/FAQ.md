-   [Quorum<span lang="zh-CN">을 사용하면서 문제가 생겼습니다</span>. <span lang="zh-CN">어디서 도움을 받을 수 있나요</span>?](#_heading=h.gjdgxs)

-   

-   [프라이빗 트랜잭션에서 Quorum<span lang="zh-CN">은 어떻게 합의를 이루나요</span>?](#_heading=h.30j0zll)

-   [프라이빗 트랜잭션에서 트랜잭션 사이즈에 대한 제한 사항(<span lang="zh-CN">트랜잭션이 암호화되어 있기 때문에</span>)<span lang="zh-CN">은 없나요</span>?](#_heading=h.1fob9te)

-   <span lang="zh-CN">[프라이빗 트랜잭션에](#_heading=h.3znysh7)[**트랜잭션을 생성한 노드도**](#_heading=h.3znysh7)[포함시켜야 하나요](#_heading=h.3znysh7)</span>[?](#_heading=h.3znysh7)

-   [트랜잭션 매니저 없이 Quorum <span lang="zh-CN">노드를 실행하는 것이 가능한가요</span>?](#_heading=h.2et92p0)

-   Raft <span lang="zh-CN">합의 노드 구성의 흔한 오류 </span>

-   [Quorum/Constellation/Tessera<span lang="zh-CN">의 공식적 도커</span>(Docker) <span lang="zh-CN">이미지가 있나요</span>?](#_heading=h.gjdgxs)

-   [Quorum <span lang="zh-CN">노드를 다른 합의를 사용하는 노드들과 혼합하여 사용해도 되나요</span>?](#_heading=h.gjdgxs)

### <span id="_heading=h.gjdgxs"></span>Quorum<span lang="zh-CN">을 사용하면서 문제가 생겼습니다</span>. <span lang="zh-CN">어디서 도움을 받을 수 있나요</span>?

Quorum<span lang="zh-CN">의 기술팀이 지속적으로 모니터링하는 곳이 두 군데 있습니다</span>. <span lang="zh-CN">이 사이트</span>, <span lang="zh-CN">관련 저장소들과 </span>Quorum Slack<span lang="zh-CN">입니다</span>. Quorum Slack<span lang="zh-CN">은 커뮤니티에 질문하고 즉각적인 해답을 얻을 수 있는 가장 효과적인 채널입니다</span>. <span lang="zh-CN">[이곳](https://clh7rniov2.execute-api.us-east-1.amazonaws.com/Express/)을 통해 바로 </span>Quorum Slack <span lang="zh-CN">채널에 가입하실 수 있습니다</span>.

### Quorum<span lang="zh-CN">은 트랜잭션의 프라이버시를 어떻게 보장하나요</span>?

Quorum<span lang="zh-CN">은 트랜잭션 프라이버시를 다음을 통해 달성합니다</span>. 1. <span lang="zh-CN">트랜잭션을 송신하는 측에서 </span>privateFor <span lang="zh-CN">파라미터를 이용하여 해당 트랜잭션을 공유할 노드들을 설정합니다</span>. 2. <span lang="zh-CN">프라이빗 트랜잭션의 페이로드</span>(payload)<span lang="zh-CN">를 암호화된 페이로드의 해시</span>(hash)<span lang="zh-CN">값으로 대체하여 원래의 페이로드를 트랜잭션 공유를 허용하지 않은 노드들에게는 보이지 않도록 합니다</span>. 3. <span lang="zh-CN">암호화된 프라이빗 데이터를 별도로 구성한 트랜잭션 매니저</span>([Constellation](https://github.com/jpmorganchase/constellation) <span lang="zh-CN">혹은 </span>[Tessera](https://github.com/jpmorganchase/tessera))<span lang="zh-CN">에 저장합니다</span>. <span lang="zh-CN">트랜잭션 매니저는 암호화된 데이터를 공유를 허용한 노드들에게 배포하고 복호화된 페이로드를 해당 노드들에게 제공합니다</span>.

\[\[<span lang="zh-CN">트랜잭션 처리 및 프라이버시</span>|<span lang="zh-CN">트랜잭션 처리</span>\]\]<span lang="zh-CN">에서 더 많은 정보를 확인할 수 있습니다</span>.

### <span id="_heading=h.30j0zll"></span><span lang="zh-CN">프라이빗 트랜잭션에서 </span>Quorum<span lang="zh-CN">은 어떻게 합의를 이루나요</span>?

<span lang="zh-CN">기본 이더리움에서는 모든 노드들이 모든 거래를 처리하기 때문에 각각의 노드가 같은 </span>state root<span lang="zh-CN">를 가지고 있습니다</span>. Quorum<span lang="zh-CN">에서는 노드들이 모든 ‘퍼블릭’ 트랜잭션</span>(<span lang="zh-CN">예로</span>, <span lang="zh-CN">참고자료나 시장 데이터 요약 등</span>)<span lang="zh-CN">은 처리 하지만 ‘프라이빗’ 트랜잭션은 허용된 노드들만 처리할 수 있습니다</span>.

Quorum <span lang="zh-CN">노드들은 두 가지 패트리샤 머클 트리</span>(Patricia Merkle Trie)<span lang="zh-CN">를 관리합니다</span>. <span lang="zh-CN">하나는 프라이빗 스테이트를 위한 것이고 또 하나는 퍼블릭 스테이트를 위한 것입니다</span>. <span lang="zh-CN">이로 인해 신규 블록을 추가할 때</span>, <span lang="zh-CN">블록 검증 단계에서 ‘퍼블릭 스테이트 루트 </span>(state root)’<span lang="zh-CN">의 스테이트 확인 과정을 거칩니다</span>. <span lang="zh-CN">또한 블록 검증 단계에는 블록의 모든 퍼블릭</span>/<span lang="zh-CN">프라이빗 트랜잭션 해시를 확인하는 ‘글로벌 트랜잭션 해시</span>(global Transaction hash)’ <span lang="zh-CN">확인 절차 또한 포함합니다</span>. <span lang="zh-CN">이는 각각의 노드가 다른 노드들과 동일한 트랜잭션 세트를 보유함을 검증할 수 있다는 것을 말합니다</span>. **EVM**<span lang="zh-CN">**은 동기화된 퍼블릭 스테이트 루트를 통해 결정되고 프라이빗 트랜잭션은 노드들 간에 동기화**</span>**(**<span lang="zh-CN">**글로벌 트랜잭션 해시 확인 절차**</span>**)** <span lang="zh-CN">**되기 때문에 모든 노드들에서 프라이빗 스테이트가 동기화된다는 것을 예상할 수 있습니다**</span>**.** <span lang="zh-CN">**또한** </span>**Quorum**<span lang="zh-CN">**은 특정 블록의 특정 트랜잭션에 있는 프라이빗 스테이트 해시를 조회하는** </span>**eth\_storageRoot** **API**<span lang="zh-CN">**를 제공하고 있습니다**</span>**.** <span lang="zh-CN">**애플리케이션 레이어에서 이** </span>**API**<span lang="zh-CN">**를 사용하여 상대방의 오프 체인 상태 검증을 수행할 수 있습니다**</span>**.**

\[\[Quorum <span lang="zh-CN">합의알고리즘</span>|Quorum<span lang="zh-CN">합의알고리즘</span>\]\]<span lang="zh-CN">와 </span>\[\[<span lang="zh-CN">트랜잭션 처리 및 프라이버시</span>|<span lang="zh-CN">트랜잭션 처리</span>\]\] <span lang="zh-CN">페이지에서 더 많은 정보를 확인할 수 있습니다</span>.

### <span id="_heading=h.1fob9te"></span><span lang="zh-CN">프라이빗 트랜잭션에서 트랜잭션 사이즈에 대한 제한 사항 </span>(<span lang="zh-CN">트랜잭션이 암호화되어 있기 때문에</span>)<span lang="zh-CN">은 없나요</span>?

<span lang="zh-CN">트랜잭션의 유일한 제한 사항은 가스 한도 </span>(gas limit)<span lang="zh-CN">입니다</span>. Constellation/Tessera<span lang="zh-CN">에서는 </span>(<span lang="zh-CN">설정이 가능은 하겠지만</span>) <span lang="zh-CN">트랜잭션 사이즈에 대한 제한이 없습니다</span>. <span lang="zh-CN">**사이즈가 큰 프라이빗 트랜잭션을 실행할 때**</span>**,** <span lang="zh-CN">**오히려 속도가 향상되는데 이는 대부분의 네트워크가 해시 값** </span>**(hash digest)**<span lang="zh-CN">**만을 보기 때문입니다**</span>**.** <span lang="zh-CN">**이 특성으로 인하여** 큰 데이터를 지리적으로 분산되어 있는 노드들에게 전파하는 속도가 </span>PGP<span lang="zh-CN">가 파일을 암호화하여 </span>http/https<span lang="zh-CN">로 전달하는 속도와 유사함으로 트랜잭션의 전달이 매우 빠르다고 볼 수 있습니다</span>. <span lang="zh-CN">순차적인 트랜잭션을 처리하는 경우라면 당연히 해당 트랜잭션들이 전달되기를 기다려야 하겠지만</span>, <span lang="zh-CN">독립적이거나 동시다발적인 트랜잭션을 처리하는 경우라면 페이로드의 크기가 전송속도에 영향을 미치지 않으므로 네트워크 대역폭</span>(network bandwidth)<span lang="zh-CN">이 트랜잭션 전송의 제한 사항이 될 수 있습니다</span>. Constellation/Tessera<span lang="zh-CN">는 모든 트랜잭션들을 동시에 처리합니다</span>.

### <span id="_heading=h.3znysh7"></span><span lang="zh-CN">프라이빗 트랜잭션에 트랜잭션을 생성한 노드도 포함시켜야 하나요</span>?

<span lang="zh-CN">아니요</span>, <span lang="zh-CN">포함시키면 안됩니다</span>. Quorum<span lang="zh-CN">에서는 트랜잭션을 생성한 노드를 </span>privateFor<span lang="zh-CN">에 포함하면 오류가 발생합니다</span>. <span lang="zh-CN">해당 트랜잭션을 생성한 노드에게만 보이는 프라이빗 컨트랙트를 만들고자 할 때는 다음의 형식만 이용하시길 바랍니다</span>: privateFor: \[\]

### <span id="_heading=h.2et92p0"></span><span lang="zh-CN">트랜잭션 매니저 없이 </span>Quorum <span lang="zh-CN">노드를 실행하는 것이 가능한가요</span>?

<span lang="zh-CN">트랜잭션 매니저</span>(Transaction Manager)<span lang="zh-CN">가 없어도 노드를 실행하는 것이 가능합니다</span>. <span lang="zh-CN">이를 위해서는 </span>Quorum <span lang="zh-CN">노드의 소켓 구성 시</span>, <span lang="zh-CN">대응되는 </span>Tessera/Constellation <span lang="zh-CN">대신 </span>PRIVATE\_CONFIG=ignore ...<span lang="zh-CN">로 셋팅해야 합니다</span>. Quorum <span lang="zh-CN">노드를 이렇게 구성하는 경우</span>, <span lang="zh-CN">노드가 해당 프라이빗 키들을 브로드캐스트하지 않기 떄문에</span>(<span lang="zh-CN">실행 중인 트랜잭션 매니저가 없는지 확인하십시오</span>) <span lang="zh-CN">프라이빗 트랜잭션을 사용할 수 없습니다</span>.

### Raft <span lang="zh-CN">합의 노드 구성의 흔한 오류 </span>

[https://github.com/jpmorganchase/quorum/issues/410](https://github.com/jpmorganchase/quorum/issues/410%EB%A5%BC) <span lang="zh-CN">를 참고해주세요</span>

### [Quorum/Constellation/Tessera<span lang="zh-CN">의 공식적 도커</span>(Docker) <span lang="zh-CN">이미지가 있나요</span>?](#bookmark=id.4d34og8)

<span lang="zh-CN">네</span>! <span lang="zh-CN">있습니다</span>. <span lang="zh-CN">공식적[도커](https://hub.docker.com/u/quorumengineering/)컨테이너</span>:

quorumengineering/quorum:latest quorumengineering/constellation:latest quorumengineering/tessera:latest

### Quorum <span lang="zh-CN">노드를 다른 합의를 사용하는 노드들과 혼합하여 사용해도 되나요</span>?

<span id="_heading=h.tyjcwt"></span> <span lang="zh-CN">아쉽지만</span>, <span lang="zh-CN">안됩니다</span>. Raft <span lang="zh-CN">합의 알고리즘을 사용하는 </span>Quorum <span lang="zh-CN">노드들은 </span>Raft <span lang="zh-CN">합의 알고리즘을 사용하는 다른 노드들과만 문제없이 상호작용할 수 있습니다</span>. <span lang="zh-CN">이것은 지원되는 모든 합의 알고리즘에 적용됩니다</span>.
