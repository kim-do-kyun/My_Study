# 네트워크 소개

<br>

## 호스트, 스위치, 라우터, 통신링크
* 호스트(host)
  * 컴퓨터 네트워크에 연결되어 응용프로그램을 실행하는 장치로 **end system**이라고도 부름
* 스위치(switch)
  * 네트워크 장치들을 연결하며, 연결된 발신 장치로부터 수신된 데이터를, MAC 주소에 기반하여, 연결된 목적지 장치(들)로 전달하는 장치
* 라우터(router)
  * 컴퓨터 네트워크들을 연결하며, 연결된 한 네트워크로부터 수신된 데이터를, IP 주소에 기반하여, 연결된 다른 네트워크로 전달하는 장치
* 통신링크(전송매체)
  * 꼬임쌍선(twisted pair cable), 광섬유케이블(optical fiber cable) 등

![스크린샷 2024-03-06 173646](https://github.com/kim-do-kyun/My_Baekjoon/assets/70315428/b4f2890c-dda3-4993-adbc-2cc3f7000ce5)

<br>

## 프로토콜
* 둘 이상 통신 개체 간 메시지 송수신 규칙 정의
* ex)
  * HTTP, DNS, DHCP, RIP, BGP
  * TCP, UDP
  * ICMP, OSPF
  * IP, ARP

<br>

## PDU(Protocol Data Unit)
* 컴퓨터 네트워크에서 동일 계층 프로토콜 간 전송되는 정보 단위
* ex)
  * TCP -> TCP세그먼트(TCP segment), 세그먼트(segment)
  * UDP -> 유저 데이터그램(user datagram)
  * IP -> 패킷(packet), IP 데이터그램(IP datagram), 데이터그램(datagram)
  * 이더넷(Ethernet) -> 프레임(frame), 이더넷 프레임

<br>

## RFC, IETF, IEEE 802
* RFC(Request For Comments)
  * IETF에 의해 출판되는 인터넷 기술 관련 문서
  * ex)
    * TCP -> RFC 793, RFC 1122, ...
    * IP -> RFC 791
    * HTTP 1.0 -> RFC 1945
    * HTTP 1.1 -> RFC 2616
  * IETF(Internet Enginnering Task Force)
    * 인터넷 표준 개발 기구
  * IEEE 802 LAN/MAN 표준위원회
    * IEEE -> Institute of Electrical and Electronics Enginners(전기전자기술자협회)
    * IEEE 802.3 워킹그룹 -> 이더넷
    * IEEE 802.11 워킹그룹 -> 무선 LAN
* 옥텟(Octet)
  * 8비트로 이루어진 정보단위를 지칭하는 용어