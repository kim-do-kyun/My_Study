# 컴퓨터 네트워크 개요

<br>

### 인터넷(Internet)
* 전세계 컴퓨팅 장치들을 연결하는 컴퓨터 네트워크(PC, 서버, 스마트폰, 태블릿, TV 등)
* 구성요소
  * 호스트(host) or 종단시스템(end system)
  * 통신링크(communication link) - 동축케이블, 광케이블, 라디오 스펙트럼 등
  * 패킷스위치(packet switch) - 라우터, 링크계층스위치
  * ISP(Internet Service Provider) - 종단시스템은 ISP를 통해 인터넷에 접속
  * 프로토콜
    * TCP/IP : 인터넷의 주요 프로토콜
    * IETF에서 RFC 문서 형식으로 표준화
    * 둘 이상 통신 개체 간 교환되는 메시지 포맷, 순서 등 정의

<br>

### ISP(Internet Service Provider)
* 종단시스템에 인터넷 접속 서비스를 제공
  * 인터넷접속기술
    * 케이블모뎀, DSL, 고속 LAN, 무선접속, 다이얼업모뎀 접속
* 물리적으로 **패킷스위치**와 **통신 링크**로 이루어진 네트워크
* ISP들도 서로 연결되어야 함
  * 하위계층 ISP들은 국가 혹은 글로벌 레벌의 상위계층 ISP에 연결

<br>

### 네트워크의 가장자리(The Network Edge)
* 종단시스템(end system) - 호스트(host)라고 함
  * 인터넷의 가장자리는 종단시스템이 차지
  * 호스트는 client와 server로 구분
  * 많은 server들은 data center 내에 위치
* 접속네트워크(access network)
  * 종단시스템이 연결된 네트워크 - **종단시스템**을 첫번째 **라우터**(first router, edge router)에 연결하는 네트워크
  * 유형
    * 가정접속 : DSL, Cable, FTTH, Dial-Up, Satelite
    * 기업 접속 : Ethernet, WiFi
    * 광역무선접속 : 3G, LTE

<br>

### 가정 인터넷 접속 기술
* DSL(Digital Subscriber Line)
  * 기존 전화 회선으로 데이터와 기존 전화신호를 동시 전달(다른 주파수 대역으로 인코딩)
  * 수백 ~ 수천 가정들이 하나의 DSLAM에 연결 - DSLAM(DSL Access Multiplexer)
  * DSL modem 필요

![스크린샷 2024-03-06 181712](https://github.com/kim-do-kyun/My_Study/assets/70315428/ec731111-aa43-4cf6-920c-21ca9147cc9b)
* HFC(케이블 인터넷 접속)
  * 케이블 TV 회사의 기존 케이블 TV 기반 구조 활용
  * 광 및 동축케이블 함께 사용됨 : HFC(Hybrid Fiber Coaxial)라고 부름
  * Cable modem 필요
  * CMTS(Cable Modem Termination System)
* FTTH(Fiber To The Home)
  * 가정까지 직접 광섬유 링크 제공
  * OLT(Optical Line Terminator)
  * 각 가정은 ONT(Optimal Network Terminator)에 홈 라우터 연결

<br>

### 기업 접속
* 이더넷(Ethernet) - 기업, 대학, 가정 인터넷 접속
* 와이파이(WiFi)

<br>

### 물리 매체
* 물리매체 상에 전자기파, 광펄스를 전파하여 비트를 전송
* 유형
  * 유도매체(guided media) - 광섬유, 꼬임쌍선, 동축케이블
  * 비유도매체(unguided media) - 대기와 야외공간
* 꼬임쌍선(twisted-pair copper wire)
  * 2개 절연동선을 전기간섭을 줄이기 위해 꼬아 둔 것(여러 꼬임쌍선이 보호물에 싸여 한 케이블내에 묶여있음)
  * UTP(Unshielded Twisted Pair) : LAN에서 가장 보편적 물리 매체
* 동축케이블(coaxial cable)
* 광섬유(fiber optics) - 비트를 나타내는 빛의 파동을 전달하는 가늘고 유연한 매체
* 지상라디오채널(terrestrial radio channel) - 전자기 스펙트럼으로 신호 전달
* 위성라디오채널(satelite radio channel) - 정지위성, 저궤도위성

<br>

### 패킷교환(packet switching) - 가서 줄서기
* 송수신측 종단시스템 간 패킷이 전송됨, 각 패킷은 통신 링크와 패킷스위치(라우터, 링크계층스위치)를 거침
* 저장 후 전달 전송(store-and-forward transmission)
  * 대부분 패킷스위치는 패킷을 모두 수신한 후 출력링크로 전달
  * 패킷전송시간(전파지연 등 다른 지연은 없다고 가정)
    * ex) 발신지에서 1개 패킷(L비트)을 목적지로 전송하는 경우 : 2L/R초
    * => 발신지와 목적지 사이에 N개 링크가 있는경우 : N*L/R (K개의 패킷은 (K-1)*L/R)
* 큐잉지연과 패킷손실
  * 패킷스위치는 각 링크에 대해 출력버퍼(출력큐)를 가짐
  * 큐잉지연(queuing delay)
    * 해당 출력링크가 다른 패킷전송중이면 도착하는 패킷은 버퍼에서 대기해야함(버퍼가 가득찬경우 새로운 패킷이 도착하면 폐기 : 패킷손실)
* 전달테이블과 라우팅프로토콜
  * 각 라우터는 패킷의 목적지주소(의 일부)를 라우터의 출력 링크로 매핑하는 forwarding table 유지

<br>

### 회선교환
* 종단 간 경로 상의 필요자원을 통신 세션동안 예약
* 다중화 : 주파수분할다중화(FDM), 시분할다중화(TDM)