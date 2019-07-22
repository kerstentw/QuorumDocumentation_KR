허가형 네트워크에서는 불필요하게 해시 파워가 낭비되는 작업 증명(PoW, Proof-of-Work)나 지분 증명(PoS,
Proof-of-Stake) 방식을 사용할 필요가 없습니다. 그렇기 때문에 Quorum은 컨소시엄 체인(허가형 네트워크)에 보다
적합한 다음과 같은 합의 메커니즘을 제공합니다:

\***Raft** **합의 알고리즘**: 빠른 블록 생성시간(blocktimes)과 거래 완결성(transaction
finality)을 가지며, 요청이 들어오는 경우에만 블록을 생성하는 합의 모델입니다. 자세한 내용은
[이더리움](https://github.com/jpmorganchase/quorum/blob/master/docs/Consensus/raft.md)[/Quorum을
위한 Raft 알고리즘에서 확인하세요.  
\***이스탄불** **BFT (Byzantine Fault Tolerance)** **합의 알고리즘**:
PBFT(Practical Byzantine Fault Tolerance)에서 영감을 받아 AMIS에서 구현한 거래 완결성을 지닌
합의 알고리즘입니다. 자세한 내용은 이스탄불 BFT 합의
알고리즘,](https://github.com/jpmorganchase/quorum/blob/master/docs/Consensus/raft.md)[RPC
API](https://github.com/getamis/go-ethereum/wiki/RPC-API), [본 기술
문서](https://medium.com/getamis/istanbul-bft-ibft-c2758b7fe6ff)에서
확인하세요.

\* **클릭** **POA**(**Clique Proof-of-Authority)** **합의 알고리즘**:
Go-ethereum(Geth)에서 기본적으로 제공하는 권위 증명(PoA) 합의 알고리즘입니다. 자세한 내용은
[클릭](https://github.com/ethereum/EIPs/issues/225)[PoA 합의
알고리즘,](https://github.com/ethereum/EIPs/issues/225)[puppeth](https://blog.ethereum.org/2017/04/14/geth-1-6-puppeth-master/),
클릭(clique) json 셋업 가이드를 확인해보세요.

